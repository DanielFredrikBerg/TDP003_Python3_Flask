<h1>Manual and oversight manual for TDP003-Portfolio project</h1>
Activate venv with: <code>source venv/bin/activate</code>
Deactivate with <code>deactivate</code>
<h2>App Catalog Structure</h2>
/portfolio_app
	setup.py
	portfolio_app.py
	/portfolio_app
		\_\_init\_\_.py
		routes.py
		/static
			style.css
		/templates
			layout.html
			index.html
			techniques.html
			...			
<h2>Errors and Solutions</h2>
Error [errno 98] address already in use flask
* ps -fA | grep python
* kill -9 \[flask pid\]
<h2>Check the issues for what to do next!</h2>
061020: Catalog structure defined. Initial @app.route() file i set up. Link to current tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


