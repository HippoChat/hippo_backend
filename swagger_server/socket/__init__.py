from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from flask import request
from flask_jwt_extended import decode_token
import flask_socketio

from swagger_server import app, socketio
from swagger_server.models import Message, MessagesResponse, SendMessageRequest, UserId
from swagger_server.service import facebook


@dataclass
class OnlineUser:
    user_id: UserId
    sid: Any


class OnlineUsersManager:

    def __init__(self) -> None:
        super().__init__()

        # self.__users_online: List[OnlineUser] = []
        self.__by_sid: Dict[str, OnlineUser] = {}

    def connect(self, user: OnlineUser) -> None:
        self.__by_sid[user.sid] = user

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
        print("not disconnecting by user id")
        pass
        # for user in self.__users_online:
        #     if user.user_id == user_id:
        #         flask_socketio.disconnect(sid=user.sid)
        #         self.__users_online.remove(user)

    def disconnect_by_sid(self, sid=None) -> None:
        if sid is None:
            sid = request.sid

        user = self.__by_sid.pop(sid)
        if user is not None:
            flask_socketio.disconnect(sid=user.sid)

    def get_all(self, user_id: UserId) -> List[OnlineUser]:
        return [
            user
            for user in self.__by_sid.values()
            if user.user_id == user_id
        ]

    def get_by_sid(self, sid=None) -> Optional[OnlineUser]:
        if sid is None:
            sid = request.sid

        print("all users online: ", self.__by_sid)

        return self.__by_sid.get(sid)


manager = OnlineUsersManager()


@socketio.on('doAuth')
def handle_connect(json):
    jwt = json['token']
    user = manager.connect_by_sid(jwt)
    app.logger.error("User authenticated: %s", user)


@socketio.on('disconnect')
def handle_disconnect():
    # manager.disconnect_by_sid()
    app.logger.error("disconnected sid: %s", request.sid)


@socketio.on('sendMessage')
def handle_message(json):
    user = manager.get_by_sid()
    if user is None:
        app.logger.error("Not authenticated sid: %s", request.sid)
        flask_socketio.disconnect()

    app.logger.error("message json: %s", json)
    body = SendMessageRequest.from_dict(json)
    recv_user = manager.get_all(body.receiver_id)
    if len(recv_user) == 0:
        return

    message = Message(
        id=123,
        timestamp=datetime.now(),
        incoming=True,
        sender=user.user_id,
        receiver=recv_user[0].user_id,
        message=body.message,
        image="",
        reply_to_message_id=None,
    ).to_dict()
    rooms = [u.sid for u in recv_user]
    for room in rooms:
        socketio.emit('newMessage', message, room=room, json=True)
