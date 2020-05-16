# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.partner_response import PartnerResponse  # noqa: E501
from swagger_server.models.sign_up_response import SignUpResponse  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_info_response import UserInfoResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_get_by_id(self):
        """Test case for user_get_by_id

        
        """
        response = self.client.open(
            '/api/user/{id}'.format(id=UserId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_set_info(self):
        """Test case for user_set_info

        Set users' info such as name, language, profile image etc.
        """
        body = UserInfo()
        response = self.client.open(
            '/api/user/set_info',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_wait_for_partner(self):
        """Test case for user_wait_for_partner

        
        """
        response = self.client.open(
            '/api/user/wait_for_partner',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
