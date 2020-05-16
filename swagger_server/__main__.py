#!/usr/bin/env python3
import flask
from flask_jwt_extended import JWTManager
import connexion
import swagger_server as this

from swagger_server import encoder


def random_str(length: int) -> str:
    import random
    import base64

    array = bytes(random.randint(0, 255) for _ in range(length))
    string = base64.b64encode(array).decode('utf8')
    return string


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'backend'}, pythonic_params=True)

    # Setup the Flask-JWT-Extended extension
    app.app.config['JWT_SECRET_KEY'] = 'super-secret' + random_str(32)  # Change this!

    this.__app = app.app
    this.__connexion = app
    this.__jwt = JWTManager(app.app)

    app.run(port=8080)


if __name__ == '__main__':
    main()
