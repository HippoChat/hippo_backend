import base64
import random

import connexion
import flask
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

from swagger_server import encoder


def random_str(length: int) -> str:
    array = bytes(random.randint(0, 255) for _ in range(length))
    string = base64.b64encode(array).decode('utf8')
    return string


# Setup Connexion + Flask application
conn = connexion.App(__name__, specification_dir='./swagger/')
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
