### Code Analyze

- Steps to Run the application
    - First , unzip the folder
    - Go to the project directory , `cd cast`
    - First Virtualenv , if not install on your system 
        -  `pip install virtualenv`
        - `virtualenv venv`
        - Now, activate the virtualenv
            - Run `source venv/bin/activate`
    - Server(Backend)
        - go to server directory -  `cd server`
        - Install some requirements to run the backend server
            - Run `pip install -r requirements.txt`
        - Run Migrations
            - `python manage.py makemigrations` - for creating initial migrations
            - `python manage.py migrate` - to create database 
        - finally , run the backend server
            - Run `python manage.py runserver`
            - It will start the django development server , locally on port number - 8000
    - Client(Frontend)
        - open a new terminal and go to the main projetct directory. `cd cast`
        - Then go to client directory - `cd client` 
        - Install some dependencies for client server
            - Run `npm install` or `yarn install`
            - if yarn not install , first install it.
                - npm install yarn
        - Now, run the Client server
            - Run `npm start` or `yarn start`
        
        - On terminal , you see the logs like
            - You can now view web in the browser.
                ```
                    Local:            http://localhost:3001/ -  will be different on your system . open this address in your  browser
                    On Your Network:  http://192.168.0.102:3001/
                ```
        - Now, open your favorite browser and type `localhost:3001`.**
        

- GitHUb Url 
    - url : https://github.com/djangoconfire/code_analyzer

