import flask
import socket
from flask import request, jsonify

docker_short_id = socket.gethostname()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

payload = [{ "message": "Hello deserve", "branches": "US, Pune, Bangalore", "containerid": docker_short_id }]

@app.route('/', methods=['GET'])
def home():
    return jsonify(payload)

app.run(host="0.0.0.0")
