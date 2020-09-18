# Deploy Flask app in Heroku

This project can be used as a base for developing web app using Flask api and deploying in Heroku . Clone the project and modify the code as per your requirement.

### Structure
Application has the following folders and files
1. <b>static folder</b> - This folder serves static files such as CSS, JS, images. In our project we have css folder, which contains .css file and image file
2. <b>templates folder</b> - This folder should have the html files, which will be rendered
3. <b>AppFlask.py</b> - This is the main file where Flask api will be initialised. In this file we map the specific URL("/") with the associated function using @app.route
4. <b>Procfile</b> - This file is mandatory for Heroku deployment, which specifies the commands that are executed by the app on startup, like specifying the web server. Procfile Format <process type>: <command>.  Here , we mentioned - "web: gunicorn AppFlask:app". gunicorn is the web server. AppFlask is the .py file where the flask api is initialised, with variable name "app"
5. <b>requirements.txt</b> - This file contains the base libraries required to deploy app on heroku. Flask-JSGlue is required iff you are using Javascript in your app. 

### Steps to deploy app in Heroku
1. git clone https://github.com/savitha91/Flask_HerokuDeploy.git
2. cd Flask_HerokuDeploy
3. heroku login
4. heroku create
5. git push heroku master
6. Navigate to app url shown in the cli 

### Common error and solutions:
1. "No web processes running" heroku error

>  This error says you are not running any web dynos. This may be due to Procfile naming. The Procfile should always be named "Procfile" without a file extension.
The Procfile must live in your app’s root directory. It does not function if placed anywhere else.

2. Permission denied (publickey).fatal: Could not read from remote repository.

> Try to login again in Heroku and test 

3. App name created will be different from the deployed application link

> Remove the apps from Heroku(heroku apps:destroy appname) . Create new app and deploy


