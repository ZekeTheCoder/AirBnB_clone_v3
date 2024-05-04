from flask import Flask
from api.v1.views import api_views

""" This is the index.py file"""

app_views = Flask(__name__)

""" Blueprint registration """

app.register_blueprint(api_views, url_prefix='/api/v1') # Register blueprint

""" Route status endpoint """
@app.route('/status')


""" Decorate new route """
@app.route('/api/v1/stats')
def retrieve_by_obj_type():
    return count()

def app_views(): # Define view func
    return {'status' : 'OK'} # Return status


