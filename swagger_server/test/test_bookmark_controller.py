# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bookmarks_list_response import BookmarksListResponse  # noqa: E501
from swagger_server.models.response_base import ResponseBase  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookmarkController(BaseTestCase):
    """BookmarkController integration test stubs"""

    def test_user_add_bookmark(self):
        """Test case for user_add_bookmark

        
        """
        response = self.client.open(
            '/api/bookmark/{id}'.format(id=UserId()),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_get_bookmarks(self):
        """Test case for user_get_bookmarks

        
        """
        response = self.client.open(
            '/api/bookmark',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_remove_bookmark(self):
        """Test case for user_remove_bookmark

        
        """
        response = self.client.open(
            '/api/bookmark/{id}'.format(id=UserId()),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
