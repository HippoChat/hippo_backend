# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.blocked_users_response import BlockedUsersResponse  # noqa: E501
from swagger_server.models.report_request import ReportRequest  # noqa: E501
from swagger_server.models.response_base import ResponseBase  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBanController(BaseTestCase):
    """BanController integration test stubs"""

    def test_ban_get_blocked(self):
        """Test case for ban_get_blocked

        
        """
        response = self.client.open(
            '/api/ban/blocked',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ban_report(self):
        """Test case for ban_report

        
        """
        body = ReportRequest()
        response = self.client.open(
            '/api/ban/report',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
