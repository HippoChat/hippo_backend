# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_info_self import UserInfoSelf  # noqa: F401,E501
from swagger_server import util


class SignUpResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, status: int, error_message: str=None, me: UserInfoSelf=None):  # noqa: E501
        """SignUpResponse - a model defined in Swagger

        :param status: The status of this SignUpResponse.  # noqa: E501
        :type status: int
        :param error_message: The error_message of this SignUpResponse.  # noqa: E501
        :type error_message: str
        :param me: The me of this SignUpResponse.  # noqa: E501
        :type me: UserInfoSelf
        """
        self.swagger_types = {
            'status': int,
            'error_message': str,
            'me': UserInfoSelf
        }

        self.attribute_map = {
            'status': 'status',
            'error_message': 'error_message',
            'me': 'me'
        }
        self._status = status
        self._error_message = error_message
        self._me = me

    @classmethod
    def from_dict(cls, dikt) -> 'SignUpResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SignUpResponse of this SignUpResponse.  # noqa: E501
        :rtype: SignUpResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> int:
        """Gets the status of this SignUpResponse.


        :return: The status of this SignUpResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this SignUpResponse.


        :param status: The status of this SignUpResponse.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def error_message(self) -> str:
        """Gets the error_message of this SignUpResponse.


        :return: The error_message of this SignUpResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message: str):
        """Sets the error_message of this SignUpResponse.


        :param error_message: The error_message of this SignUpResponse.
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def me(self) -> UserInfoSelf:
        """Gets the me of this SignUpResponse.


        :return: The me of this SignUpResponse.
        :rtype: UserInfoSelf
        """
        return self._me

    @me.setter
    def me(self, me: UserInfoSelf):
        """Sets the me of this SignUpResponse.


        :param me: The me of this SignUpResponse.
        :type me: UserInfoSelf
        """

        self._me = me
