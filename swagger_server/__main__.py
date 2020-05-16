#!/usr/bin/env python3
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'backend'}, pythonic_params=True)

    # Setup the Flask-JWT-Extended extension
    app.app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
    jwt = JWTManager(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
