import base64
import random

import connexion
import flask
from flask_jwt_extended import JWTManager
from flask import render_template
from flask_socketio import SocketIO

from swagger_server import encoder
import pathlib


def random_str(length: int) -> str:
    array = bytes(random.randint(0, 255) for _ in range(length))
    string = base64.b64encode(array).decode('utf8')
    return string


server_args = {
    'static_url_path': str(pathlib.Path('.').joinpath('static').absolute()),
}

print(server_args)
# Setup Connexion + Flask application
conn = connexion.App(__name__, specification_dir='./swagger/', server_args=server_args)
"""
Global connexion application instance.
"""
conn.add_api('swagger.yaml', arguments={'title': 'backend'}, pythonic_params=True)


app: flask.Flask = conn.app
"""
Global Flask application instance.
"""
app.json_encoder = encoder.JSONEncoder


# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)
"""
Global JWT manager instance.
"""
app.config['JWT_SECRET_KEY'] = 'super-secret' + random_str(32)


# SocketIO
socketio = SocketIO(app)
"""
Global SocketIO instance.
"""

import swagger_server.socket


@app.route('/session')
def hello_world():
    return app.send_static_file("session.html")


from swagger_server.service import heart