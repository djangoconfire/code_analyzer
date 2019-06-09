import React, { Component } from 'react';
import axios from 'axios';
import Select from 'react-select';
import { CONSTANTS } from '../common/constants';

class CodeAnalyze extends Component {
	state = {
		file: '',
		error: '',
		output: '',
		analysis_of: '',
		text: '',
		disableSubmit: false,
		languageOptions: [
			{ value: 'py', label: 'Python' },
			{ value: 'cpp', label: 'C++' },
			{ value: 'js', label: 'Javascript' }
		],
		selectedOption: ''
	};

	submitData = () => {
		let formData = new FormData();
		if (this.state.analysis_of === 'file' && this.state.file !== '') {
			formData.set('file', this.state.file);
		} else if (this.state.analysis_of === 'text' && this.state.text !== '') {
			formData.set('text', this.state.text);
		} else {
			return;
		}
		console.log('selected option', this.state.selectedOption);
		console.log('selected option', this.state.analysis_of);

		formData.set('analysis_of', this.state.analysis_of);
		formData.set('language', this.state.selectedOption.value);
		console.log('formdata', formData);
		axios
			.post(CONSTANTS.SERVER_URL + '/api/code_analyze/', formData, {
				headers: {
					'Content-Type': 'multipart/form-data'
				}
			})
			.then((response) => {
				this.setState({
					error: '',
					disableSubmit: false,
					output: response.data.output + '\n' + response.data.error
				});

				if (this.state.output.length === 1) {
					this.setState({
						output: 'There was no output'
					});
				}
			})
			.catch(() => {
				this.setState({
					error: '',
					disableSubmit: false,
					output: 'Server Error'
				});
			});
	};

	handleChange = (selectedOption) => {
		this.setState({ selectedOption });
	};

	handleText = (e) => {
		this.setState({
			text: e.target.value
		});
	};

	handleCheckBox = (e) => {
		if (e.target.id === 'file') {
			this.setState({
				analysis_of: 'file'
			});
		} else {
			this.setState({
				analysis_of: 'text'
			});
		}
	};

	handleFileUpload = (e) => {
		this.state.file = this.$refs.file.files[0];
		if (this.file.size > 100000 || !this.file.type.match(/^text\//) || this.file.type === '') {
			this.file = '';
			this.error = 'Invalid file or it has an invalid type';
		} else {
			this.error = '';
		}
	};

	render() {
		const { selectedOption, languageOptions, analysisOptions, analysis_of } = this.state;
		return (
			<div className="code-analyze container">
				<div className="container">
					<h3 className="center blue-text">Code Analysis</h3>
					<div className="large-8 medium-8 small- cell">
						<div className="input-field">
							<p>
								<label>
									<input type="checkbox" id="file" onChange={this.handleCheckBox} />
									<span>Upload File</span>
								</label>
							</p>
						</div>
						<div className="input-field">
							<p>
								<label>
									<input type="checkbox" id="text" onChange={this.handleCheckBox} />
									<span>Text</span>
								</label>
							</p>
						</div>
						<label htmlFor="lang" className="blue-text">
							Language
						</label>
						<div className="input-field col s12">
							<Select value={selectedOption} onChange={this.handleChange} options={languageOptions} />
						</div>
						<span className="center blue-text">Upload File</span>
						<div>
							<textarea style={{ width: '500px', height: '500px' }} onChange={this.handleText} />
							<label>
								File(Size limit is 100,000 bytes)
								<input type="file" id="file" onChange={this.handleFileUpload} />
							</label>
						</div>
						<br />
						<div>
							<button
								onClick={this.submitData}
								className="btn waves-effect waves-light"
								type="submit"
								name="action"
							>
								Submit
							</button>
						</div>
						<div style={{ color: 'red' }}>{this.state.error}</div>
						<br />
						<hr />
						<div>
							Output: <pre>{this.state.output}</pre>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

export default CodeAnalyze;
