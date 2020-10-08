from flask import render_template, request, redirect, url_for
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
	if request.args.get("search projects", ""):
		return redirect(url_for("list"))
	else:
		user = {'username': 'jenoh242 & danhu849'}
		return render_template('index.html', user=user)

# /list
@app.route('/list')
def list():
	search_for = request.args.get("search projects", "")
	search_fields = request.args.getlist("search_field")
	if not search_fields:
		search_fields = None
	sort_by = request.args.get("sort_by", "")
	if not sort_by:
		sort_by= "start_date"
	sort_order = request.args.get("sort_order", "")
	if not sort_order:
		sort_order = "desc"
	techniques = request.args.getlist("technique")
	db = jen_api.load(data_path)
	found = jen_api.search(db, search=search_for, sort_by=sort_by, sort_order=sort_order, techniques=techniques, search_fields=search_fields)
	search_fields = jen_api.get_search_fields(db)
	#print(found)
	return render_template('list.html', title='Search', search_results=found, search_fields = search_fields)


# /project/id
@app.route('/project/<int:id>', methods=['GET'])
def show_project(id):
	print("this is idddddddddd", id)
	db = jen_api.load(data_path)
	chosen_project = jen_api.get_project(db, id)
	print(chosen_project)
	return render_template('project_page.html', title=chosen_project['project_name'], project=chosen_project)

# /techniques
@app.route('/techniques', methods=['GET', 'POST'])
def techniques():
	db = jen_api.load(data_path)
	db_techniques = jen_api.get_techniques(db)
	# Denna skiten är hårdkodad så det funkar, men variation måste fortfarande implementeras!
	# Det går heller ej att klicka på flera knappar.
	wanted_technique = request.form.get('ada')
	if wanted_technique:
		found = jen_api.search(db, techniques=wanted_technique)
		return render_template('techniques.html', title='Techniques', techniques=db_techniques, search_results=found)
	else:
		return render_template('techniques.html', title='Techniques', techniques=db_techniques)

# /404
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

# ERROR SOLUTIONS:

# invalid json: [Errno 2] No such file or directory: data.json
# Solution: Terminal position and flask app has to be run (flask run) from the same folder where the data.json folder is located. The api file needs to be in the same folder as the portfolio_app.py for some reason? It can't be in the same folder as the __init__ file at least. At the moment of this writing the ONLY folder "flask run" can be run from is: tdp003/portfolio_app/

# Kill app with Ctrl c otherwise risk for error below:
# Solution Error [errno 98] address already in use flask
# ps -fA | grep python
# kill -9 [pid]
