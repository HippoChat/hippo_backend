# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.response_base import ResponseBase  # noqa: E501
from swagger_server.models.sign_up_request import SignUpRequest  # noqa: E501
from swagger_server.models.sign_up_response import SignUpResponse  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server.models.verification_code_request import VerificationCodeRequest  # noqa: E501
from swagger_server.models.verify_phone_code_request import VerifyPhoneCodeRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth_send_verification_code(self):
        """Test case for auth_send_verification_code

        
        """
        body = VerificationCodeRequest()
        response = self.client.open(
            '/api/auth/send_verification_code',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_sign_up(self):
        """Test case for auth_sign_up

        
        """
        body = SignUpRequest()
        response = self.client.open(
            '/api/auth/sign_up',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_verify_phone_code(self):
        """Test case for auth_verify_phone_code

        
        """
        body = VerifyPhoneCodeRequest()
        response = self.client.open(
            '/api/auth/verify_phone_code',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_logout(self):
        """Test case for user_logout

        
        """
        response = self.client.open(
            '/api/auth/logout'.format(id=UserId()),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
