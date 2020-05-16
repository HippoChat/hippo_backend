import connexion
import six

from swagger_server.models.bookmarks_list_response import BookmarksListResponse  # noqa: E501
from swagger_server.models.response_base import ResponseBase  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server import util


def user_add_bookmark():  # noqa: E501
    """user_add_bookmark

    Adds a dialog with a given user to the current user’s bookmarks list. # noqa: E501

    :param id: ID of a user
    :type id: int

    :rtype: ResponseBase
    """
    return 'do some magic!'


def user_get_bookmarks():  # noqa: E501
    """user_get_bookmarks

    Retrieve a list of user’s bookmarked dialogs # noqa: E501


    :rtype: BookmarksListResponse
    """
    return 'do some magic!'


def user_remove_bookmark(id):  # noqa: E501
    """user_remove_bookmark

    Removes a dialog with a given user from the current user&#x27;s bookmarks list. # noqa: E501

    :param id: ID of a user
    :type id: dict | bytes

    :rtype: ResponseBase
    """
    return 'do some magic!'
