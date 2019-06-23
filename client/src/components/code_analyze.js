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
		textSelected: false,
		fileSelected: false,
		disableSubmit: false,
		languageOptions: [ { value: 'py', label: 'Python' }, { value: 'js', label: 'Javascript' } ],
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

		formData.set('analysis_of', this.state.analysis_of);
		formData.set('language', this.state.selectedOption.value);
		formData.append('file', this.state.file);
		console.log('formdata', formData, this.state.file.name);
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
						output: 'No Output'
					});
				}
			})
			.catch(() => {
				this.setState({
					error: '',
					disableSubmit: false,
					output: 'Internal Server Error'
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
				analysis_of: 'file',
				fileSelected: true,
				textSelected: false
			});
		} else {
			this.setState({
				analysis_of: 'text',
				textSelected: true,
				fileSelected: false
			});
		}
	};

	handleFileUpload = (e) => {
		this.setState({
			file: e.target.files[0]
		});
		if (this.state.file.size > 100000) {
			this.setState({
				file: '',
				error: 'Invalid file or it has an invalid type'
			});
		} else {
			this.setState({
				error: ''
			});
		}
	};

	render() {
		const { selectedOption, languageOptions, textSelected, fileSelected } = this.state;

		return (
			<div className="code-analyze container">
				<div className="container">
					<br />
					<h3 className="center blue-text">Code Analysis</h3>
					<div className="row">
						<div className="col-md-8 col-lg-8 col-sm-8">
							<div className="input-field">
								<p>
									<label>
										<input
											type="checkbox"
											id="file"
											onChange={this.handleCheckBox}
											checked={fileSelected}
										/>
										<span>Upload File</span>
									</label>
								</p>
							</div>
							<div className="input-field">
								<p>
									<label>
										<input
											type="checkbox"
											id="text"
											onChange={this.handleCheckBox}
											checked={textSelected}
										/>
										<span>Text</span>
									</label>
								</p>
							</div>
							{textSelected ? (
								<div className="row">
									<div className="col-md-8 col-lg-8 col-sm-8">
										<label htmlFor="lang" className="blue-text">
											Language
										</label>
										<Select
											value={selectedOption}
											onChange={this.handleChange}
											options={languageOptions}
										/>
										<br />
										<textarea
											style={{ width: '440px', height: '200px' }}
											onChange={this.handleText}
											placeholder="Paste the Code here..."
										/>
										<br />
										<button
											onClick={this.submitData}
											className="btn waves-effect waves-light"
											type="submit"
											name="action"
										>
											Submit
										</button>
									</div>
								</div>
							) : (
								<div>
									<label>
										File(Size limit is 100 KB)
										<input type="file" id="file" onChange={this.handleFileUpload} />
									</label>
									<br />
									<br />
									<button
										onClick={this.submitData}
										className="btn waves-effect waves-light"
										type="submit"
										name="action"
									>
										Submit
									</button>
								</div>
							)}
							<br />
						</div>

						<div className="col-md-4 col-lg-4 col-sm-4">
							Output:
							{this.state.output ? <pre>{this.state.output}</pre> : ''}
						</div>
					</div>
				</div>
			</div>
		);
	}
}

export default CodeAnalyze;
