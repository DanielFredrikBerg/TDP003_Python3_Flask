from setuptools import setup

setup(
    name='portfolio_app',
    packages=['portfolio_app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
# https://flask.palletsprojects.com/en/1.1.x/patterns/packages/
#In order to run the application you need to export an environment variable that tells Flask where to find the application instance:

# $ export FLASK_APP=portfolio_app

# For Debug mode
# $ export FLASK_ENV=development
    
