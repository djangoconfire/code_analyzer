### Code Analyze

- Steps to Run the application
    - First , unzip the folder
    - Server(Backend)
        - go to `server` directory -  cd server
        - Install some requirements to run the backend server
            - Run `pip install -r requirements.txt`
        - Run Migrations
            - python manage.py makemigrations` - Run initial migrations
            - `python manage.py migrate` - to create database 
        - finally , run the backedn server
            - Run `python manage.py runserver`
            - It will start the django development server , locally on port number - 8000
    - Client(Frontend)
        - First go to `client` directory - cd client 
        - Install some dependencies for client server
            - Run `npm install` or `yarn install`
            - if yarn not install , first install it.
                - npm install yarn
        - Now, run the Client server
            - Run `npm start` or `yarn start`
    - Now, open your favorite browser and type `localhost:3000`.**

    - GitHUb Url 
        - url : https://github.com/djangoconfire/code_analyzer

