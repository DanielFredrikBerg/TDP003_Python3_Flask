from flask import render_template
from portfolio_app import app
import jen_api
import os

current_path = os.path.dirname(__name__)
data_path = os.path.relpath('data.json', current_path)
db = jen_api.load(data_path)

# /
@app.route('/')
@app.route('/home')
def home():
	user= {'username': 'jenoh242 & danhu849'}
	return render_template('index.html', user=user)

# /list
@app.route('/list')
def list():
	return render_template('list.html', title='Search', db=db)


# /project/id
@app.route('/project/id')
def project():
	return render_template('project_page.html', title='Projects', db=db)


# /techniques
@app.route('/techniques')
def techniques():
	return render_template('techniques.html', title='Techniques', db=db)

# ERROR SOLUTIONS:

# invalid json: [Errno 2] No such file or directory: data.json
# Solution: Terminal position and flask app has to be run (flask run) from the same folder where the data.json folder is located. The api file needs to be in the same folder as the portfolio_app.py for some reason? It can't be in the same folder as the __init__ file at least. At the moment of this writing the ONLY folder "flask run" can be run from is: tdp003/portfolio_app/

# Kill app with Ctrl c otherwise risk for error below:
# Solution Error [errno 98] address already in use flask
# ps -fA | grep python
# kill -9 [pid]
