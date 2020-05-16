# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.phone import Phone  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class UserInfoSelfPrivate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, phone: Phone=None, token: str=None):  # noqa: E501
        """UserInfoSelfPrivate - a model defined in Swagger

        :param phone: The phone of this UserInfoSelfPrivate.  # noqa: E501
        :type phone: Phone
        :param token: The token of this UserInfoSelfPrivate.  # noqa: E501
        :type token: str
        """
        self.swagger_types = {
            'phone': Phone,
            'token': str
        }

        self.attribute_map = {
            'phone': 'phone',
            'token': 'token'
        }
        self._phone = phone
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'UserInfoSelfPrivate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserInfoSelf_private of this UserInfoSelfPrivate.  # noqa: E501
        :rtype: UserInfoSelfPrivate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def phone(self) -> Phone:
        """Gets the phone of this UserInfoSelfPrivate.


        :return: The phone of this UserInfoSelfPrivate.
        :rtype: Phone
        """
        return self._phone

    @phone.setter
    def phone(self, phone: Phone):
        """Sets the phone of this UserInfoSelfPrivate.


        :param phone: The phone of this UserInfoSelfPrivate.
        :type phone: Phone
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def token(self) -> str:
        """Gets the token of this UserInfoSelfPrivate.

        Authentication token  # noqa: E501

        :return: The token of this UserInfoSelfPrivate.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this UserInfoSelfPrivate.

        Authentication token  # noqa: E501

        :param token: The token of this UserInfoSelfPrivate.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token