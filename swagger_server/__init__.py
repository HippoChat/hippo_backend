import flask
import connexion
import flask_jwt_extended

__app: flask.Flask
__connexion: connexion.App
__jwt: flask_jwt_extended.JWTManager


def app() -> flask.Flask:
    global __app
    assert __app is not None
    return __app


def connexion() -> connexion.App:
    global __connexion
    assert __connexion is not None
    return __connexion


def jwt() -> flask_jwt_extended.JWTManager:
    global __jwt
    assert __jwt is not None
    return __jwt
