# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.image import Image  # noqa: F401,E501
from swagger_server.models.message_id import MessageId  # noqa: F401,E501
from swagger_server.models.user_id import UserId  # noqa: F401,E501
from swagger_server import util


class Message(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: MessageId=None, timestamp: datetime=None, incoming: bool=None, sender: UserId=None, receiver: UserId=None, message: str=None, image: Image=None, reply_to_message_id: MessageId=None):  # noqa: E501
        """Message - a model defined in Swagger

        :param id: The id of this Message.  # noqa: E501
        :type id: MessageId
        :param timestamp: The timestamp of this Message.  # noqa: E501
        :type timestamp: datetime
        :param incoming: The incoming of this Message.  # noqa: E501
        :type incoming: bool
        :param sender: The sender of this Message.  # noqa: E501
        :type sender: UserId
        :param receiver: The receiver of this Message.  # noqa: E501
        :type receiver: UserId
        :param message: The message of this Message.  # noqa: E501
        :type message: str
        :param image: The image of this Message.  # noqa: E501
        :type image: Image
        :param reply_to_message_id: The reply_to_message_id of this Message.  # noqa: E501
        :type reply_to_message_id: MessageId
        """
        self.swagger_types = {
            'id': MessageId,
            'timestamp': datetime,
            'incoming': bool,
            'sender': UserId,
            'receiver': UserId,
            'message': str,
            'image': Image,
            'reply_to_message_id': MessageId
        }

        self.attribute_map = {
            'id': 'id',
            'timestamp': 'timestamp',
            'incoming': 'incoming',
            'sender': 'sender',
            'receiver': 'receiver',
            'message': 'message',
            'image': 'image',
            'reply_to_message_id': 'reply_to_message_id'
        }
        self._id = id
        self._timestamp = timestamp
        self._incoming = incoming
        self._sender = sender
        self._receiver = receiver
        self._message = message
        self._image = image
        self._reply_to_message_id = reply_to_message_id

    @classmethod
    def from_dict(cls, dikt) -> 'Message':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Message of this Message.  # noqa: E501
        :rtype: Message
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> MessageId:
        """Gets the id of this Message.


        :return: The id of this Message.
        :rtype: MessageId
        """
        return self._id

    @id.setter
    def id(self, id: MessageId):
        """Sets the id of this Message.


        :param id: The id of this Message.
        :type id: MessageId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this Message.


        :return: The timestamp of this Message.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this Message.


        :param timestamp: The timestamp of this Message.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def incoming(self) -> bool:
        """Gets the incoming of this Message.

        Shortcut for comparing sender with current user's ID.  # noqa: E501

        :return: The incoming of this Message.
        :rtype: bool
        """
        return self._incoming

    @incoming.setter
    def incoming(self, incoming: bool):
        """Sets the incoming of this Message.

        Shortcut for comparing sender with current user's ID.  # noqa: E501

        :param incoming: The incoming of this Message.
        :type incoming: bool
        """

        self._incoming = incoming

    @property
    def sender(self) -> UserId:
        """Gets the sender of this Message.


        :return: The sender of this Message.
        :rtype: UserId
        """
        return self._sender

    @sender.setter
    def sender(self, sender: UserId):
        """Sets the sender of this Message.


        :param sender: The sender of this Message.
        :type sender: UserId
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def receiver(self) -> UserId:
        """Gets the receiver of this Message.


        :return: The receiver of this Message.
        :rtype: UserId
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: UserId):
        """Sets the receiver of this Message.


        :param receiver: The receiver of this Message.
        :type receiver: UserId
        """
        if receiver is None:
            raise ValueError("Invalid value for `receiver`, must not be `None`")  # noqa: E501

        self._receiver = receiver

    @property
    def message(self) -> str:
        """Gets the message of this Message.


        :return: The message of this Message.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Message.


        :param message: The message of this Message.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def image(self) -> Image:
        """Gets the image of this Message.


        :return: The image of this Message.
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image: Image):
        """Sets the image of this Message.


        :param image: The image of this Message.
        :type image: Image
        """

        self._image = image

    @property
    def reply_to_message_id(self) -> MessageId:
        """Gets the reply_to_message_id of this Message.


        :return: The reply_to_message_id of this Message.
        :rtype: MessageId
        """
        return self._reply_to_message_id

    @reply_to_message_id.setter
    def reply_to_message_id(self, reply_to_message_id: MessageId):
        """Sets the reply_to_message_id of this Message.


        :param reply_to_message_id: The reply_to_message_id of this Message.
        :type reply_to_message_id: MessageId
        """

        self._reply_to_message_id = reply_to_message_id
