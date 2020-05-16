from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enum import Enum
from base64 import b64decode, b64encode

UserId = int
MessageId = int


class AgeGroup(Enum):
    Younger_18 = "<18"
    Range_18_25 = "18-25"
    Range_26_35 = "26-35"
    Range_36_45 = "36-45"
    Older_45 = ">45"


@dataclass
class UserPrivate:
    phone: str
    token: str

    @staticmethod
    def from_json(json: dict) -> 'UserPrivate':
        return UserPrivate(
            phone=json['phone'],
            token=json['token'],
        )

    def to_json(self) -> dict:
        return {
            'phone': self.phone,
            'token': self.token,
        }


@dataclass
class UserInfo:
    id: int
    name: str
    age_group: AgeGroup
    language: str
    image: bytes

    @staticmethod
    def from_json(json: dict) -> 'UserInfo':
        return UserInfo(
            id=json['id'],
            name=json['name'],
            age_group=AgeGroup(json['age_group']),
            language=json['language'],
            image=b64decode(json['image'])
        )

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'age_group': str(self.age_group),
            'language': self.language,
            'image': b64encode(self.image),
        }


@dataclass
class User:
    public: UserInfo
    private: UserPrivate

    @staticmethod
    def from_json(json) -> 'User':
        return User(
            public=json['public'],
            private=json['private'],
        )

    def to_json(self) -> dict:
        return {
            'public': self.public.to_json(),
            'private': self.private.to_json(),
        }


@dataclass
class Message:
    id: MessageId
    timestamp: datetime
    sender: UserId
    receiver: UserId
    message: Optional[str]
    image: Optional[bytes]
    reply_to_message_id: Optional[MessageId]

    @staticmethod
    def from_json(json) -> 'Message':
        this = Message(
            id=json['id'],
            timestamp=json['timestamp'],
            sender=json['sender'],
            receiver=json['receiver'],
            message=None,
            image=None,
            reply_to_message_id=None,
        )
        if 'message' in json:
            this.message = json['message']
        if 'image' in json:
            this.image = b64decode(json['image'])
        if 'reply_to_message_id' in json:
            this.reply_to_message_id = json['reply_to_message_id']
        return this

    def to_json(self) -> object:
        json = {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'sender': self.sender,
            'receiver': self.receiver,
        }
        if self.message:
            json['message'] = self.message
        if self.image:
            json['image'] = b64encode(self.image)
        if self.reply_to_message_id:
            json['reply_to_message_id'] = self.reply_to_message_id
        return json
