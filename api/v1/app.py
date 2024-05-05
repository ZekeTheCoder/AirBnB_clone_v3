#!/usr/bin/python3

from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
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
def teardown_request()


storage.close()


@app.errorhandler(404)
def err404(error):
    """ Handle 404 """
    return jsonify(err404_msg), 404


app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, threaded=True, host=host, port=port)
