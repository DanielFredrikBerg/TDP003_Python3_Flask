from flask import Flask

app = Flask(__name__)

import portfolio_app.routes

# The script above simply creates the application object as an instance of class Flask imported from the flask package. The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used. Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files, which I will cover in Chapter 2. For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way. The application then imports the routes module, which doesn't exist yet.

#Source: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
