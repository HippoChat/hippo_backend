# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.message_id import MessageId  # noqa: F401,E501
from swagger_server.models.user_id import UserId  # noqa: F401,E501
from swagger_server import util


class SendMessageRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, receiver_id: UserId=None, message: str=None, image: bytearray=None, reply_to_message_id: MessageId=None):  # noqa: E501
        """SendMessageRequest - a model defined in Swagger

        :param receiver_id: The receiver_id of this SendMessageRequest.  # noqa: E501
        :type receiver_id: UserId
        :param message: The message of this SendMessageRequest.  # noqa: E501
        :type message: str
        :param image: The image of this SendMessageRequest.  # noqa: E501
        :type image: bytearray
        :param reply_to_message_id: The reply_to_message_id of this SendMessageRequest.  # noqa: E501
        :type reply_to_message_id: MessageId
        """
        self.swagger_types = {
            'receiver_id': UserId,
            'message': str,
            'image': bytearray,
            'reply_to_message_id': MessageId
        }

        self.attribute_map = {
            'receiver_id': 'receiver_id',
            'message': 'message',
            'image': 'image',
            'reply_to_message_id': 'reply_to_message_id'
        }
        self._receiver_id = receiver_id
        self._message = message
        self._image = image
        self._reply_to_message_id = reply_to_message_id

    @classmethod
    def from_dict(cls, dikt) -> 'SendMessageRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SendMessageRequest of this SendMessageRequest.  # noqa: E501
        :rtype: SendMessageRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def receiver_id(self) -> UserId:
        """Gets the receiver_id of this SendMessageRequest.


        :return: The receiver_id of this SendMessageRequest.
        :rtype: UserId
        """
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id: UserId):
        """Sets the receiver_id of this SendMessageRequest.


        :param receiver_id: The receiver_id of this SendMessageRequest.
        :type receiver_id: UserId
        """
        if receiver_id is None:
            raise ValueError("Invalid value for `receiver_id`, must not be `None`")  # noqa: E501

        self._receiver_id = receiver_id

    @property
    def message(self) -> str:
        """Gets the message of this SendMessageRequest.


        :return: The message of this SendMessageRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SendMessageRequest.


        :param message: The message of this SendMessageRequest.
        :type message: str
        """

        self._message = message

    @property
    def image(self) -> bytearray:
        """Gets the image of this SendMessageRequest.


        :return: The image of this SendMessageRequest.
        :rtype: bytearray
        """
        return self._image

    @image.setter
    def image(self, image: bytearray):
        """Sets the image of this SendMessageRequest.


        :param image: The image of this SendMessageRequest.
        :type image: bytearray
        """

        self._image = image

    @property
    def reply_to_message_id(self) -> MessageId:
        """Gets the reply_to_message_id of this SendMessageRequest.


        :return: The reply_to_message_id of this SendMessageRequest.
        :rtype: MessageId
        """
        return self._reply_to_message_id

    @reply_to_message_id.setter
    def reply_to_message_id(self, reply_to_message_id: MessageId):
        """Sets the reply_to_message_id of this SendMessageRequest.


        :param reply_to_message_id: The reply_to_message_id of this SendMessageRequest.
        :type reply_to_message_id: MessageId
        """

        self._reply_to_message_id = reply_to_message_id