from portfolio_app import app

# /
@app.route('/')
@app.route('/home')
def home():
    return "Welcome Home"


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
