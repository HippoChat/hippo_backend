import connexion
import six

from swagger_server.models.messages_response import MessagesResponse  # noqa: E501
from swagger_server.models.send_message_request import SendMessageRequest  # noqa: E501
from swagger_server.models.sent_message import SentMessage  # noqa: E501
from swagger_server import util


def chat_poll_messages():  # noqa: E501
    """chat_poll_messages

    Poll for new messages in all chats. This may be a form of long polling. # noqa: E501


    :rtype: MessagesResponse
    """
    return 'do some magic!'


def chat_send_message(body):  # noqa: E501
    """chat_send_message

    Sends a message to another user. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SentMessage
    """
    if connexion.request.is_json:
        body = SendMessageRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
