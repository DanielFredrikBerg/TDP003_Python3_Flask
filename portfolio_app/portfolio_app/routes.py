from flask import render_template
from portfolio_app import app
import daniel_api

# /
@app.route('/')
@app.route('/home')
def home():
    user= {'username': 'Daniel'}
    return render_template('index.html', title='Home', user=user)


# /list
@app.route('/list')
def list():
    return "This is /list"


# /project/id
@app.route('/project/id')
def project():
    return "This is /project/id"


# /techniques
@app.route('/techniques')
def techniques():
    return "This is /techniques"



# Kill app with Ctrl c otherwise risk for error below:
# Solution Error [errno 98] address already in use flask
# ps -fA | grep python
# kill -9 [pid]
