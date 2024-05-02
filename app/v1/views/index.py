from flask import Flask
from api.v1.views import api_views

app_views = Flask(__name__)

app.register_blueprint(api_views, url_prefix='/api/v1') # Register blueprint

@app.route('/status') # Route status endpoint

def app_views(): # Define view func
    return {'status' : 'OK'} # Return status


