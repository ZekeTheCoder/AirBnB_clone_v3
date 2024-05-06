#!/usr/bin/python3
"""
This script creates and configures the Flask application
for the AirBnB clone v1 API.
"""
from os import getenv
from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

""" variables to keep code short """

err404_msg = {"error": "Not found"}

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_request(obj):
    """Close the database connection after each request."""
    storage.close()


@app.errorhandler(404)
def err404(error):
    """ Handle 404 errors"""
    return jsonify(err404_msg), 404


# Swagger documentation configuration
app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

# initializes Swagger documentation
Swagger(app)

if __name__ == '__main__':
    host = getenv('HOST', '0.0.0.0')
    port = int(getenv('PORT', 8000))
    app.run(debug=True, threaded=True, host=host, port=port)
