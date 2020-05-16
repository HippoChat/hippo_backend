import connexion

from swagger_server.models.blocked_users_response import BlockedUsersResponse  # noqa: E501
from swagger_server.models.report_request import ReportRequest  # noqa: E501
from swagger_server.models.response_base import ResponseBase  # noqa: E501
from swagger_server import util


def ban_get_blocked():  # noqa: E501
    """ban_get_blocked

    Get a list of users blocked by the current user. # noqa: E501


    :rtype: BlockedUsersResponse
    """
    return 'do some magic!'


def ban_report(body=None):  # noqa: E501
    """ban_report

    Reports another user as having \&quot;bad behaviour\&quot; and adds them to the list of users blocked by the given user. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ResponseBase
    """
    if connexion.request.is_json:
        body = ReportRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
