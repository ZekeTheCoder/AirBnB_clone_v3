from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views
import os
""" variables to keep code short """

err404_msg = { "error": "Not found" }

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_request()
    storage.close()
""" Handle 404 """
@app.errorhandler(404)
def err404(error):
    return jsonify(err404_msg), 404

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, threaded=True, host=host, port=port)
