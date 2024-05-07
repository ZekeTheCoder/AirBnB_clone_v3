#!/usr/bin/python3
"""
This script creates and configures the Flask application
for the AirBnB clone v1 API.
"""
from os import getenv
from flask_cors import CORS
from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_request(obj):
    """Close the database connection after each request."""
    storage.close()


@app.errorhandler(404)
def err404(error):
    """ Handle 404 errors"""
    return (jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, threaded=True, host=host, port=port)
