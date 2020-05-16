from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from flask import request
from flask_jwt_extended import decode_token
import flask_socketio

from swagger_server import app, socketio
from swagger_server.models import UserId
from swagger_server.service import facebook


@dataclass
class OnlineUser:
    user_id: UserId
    sid: Any


class OnlineUsersManager:

    def __init__(self) -> None:
        super().__init__()

        self.__users_online: List[OnlineUser] = []

    def connect(self, user: OnlineUser) -> None:
        self.disconnect(user.user_id)
        self.__users_online.append(user)

    def connect_by_sid(self, jwt: str, sid=None) -> OnlineUser:
        if sid is None:
            sid = request.sid

        raw = decode_token(jwt)
        user_id = raw['identity']
        user = facebook.load_user_by_id(user_id)
        if user is None:
            raise LookupError("User not found: id %d", user_id)

        online_user = OnlineUser(
            user_id=user.id,
            sid=sid,
        )

        self.connect(online_user)
        return online_user

    def disconnect(self, user_id: UserId) -> None:
        for user in self.__users_online:
            if user.user_id == user_id:
                flask_socketio.disconnect(sid=user.sid)

    def disconnect_by_sid(self, sid=None) -> None:
        if sid is None:
            sid = request.sid

        to_remove = []
        for user in self.__users_online:
            if user.sid == sid:
                to_remove.append(user)
        for user in to_remove:
            self.__users_online.remove(user)
            flask_socketio.disconnect(sid=user.sid)

    def get(self, user_id: UserId) -> Optional[OnlineUser]:
        for user in self.__users_online:
            if user.user_id == user_id:
                return user

    def get_by_sid(self, sid=None) -> Optional[OnlineUser]:
        if sid is None:
            sid = request.sid

        for user in self.__users_online:
            if user.sid == sid:
                return user


manager = OnlineUsersManager()


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)


@socketio.on('my auth')
def handle_connect(json):
    jwt = json['token']
    user = manager.connect_by_sid(jwt)
    print("User connected", user)


@socketio.on('disconnect')
def handle_disconnect():
    manager.disconnect_by_sid()
    print("disconnected")
