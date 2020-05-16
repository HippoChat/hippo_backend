# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.messages_response import MessagesResponse  # noqa: E501
from swagger_server.models.send_message_request import SendMessageRequest  # noqa: E501
from swagger_server.models.sent_message import SentMessage  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChatController(BaseTestCase):
    """ChatController integration test stubs"""

    def test_chat_poll_messages(self):
        """Test case for chat_poll_messages

        
        """
        response = self.client.open(
            '/api/chat/messages',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_chat_send_message(self):
        """Test case for chat_send_message

        
        """
        body = SendMessageRequest()
        response = self.client.open(
            '/api/chat/send_message',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
