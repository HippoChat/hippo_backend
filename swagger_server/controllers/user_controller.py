import connexion
import six

from swagger_server.models.partner_response import PartnerResponse  # noqa: E501
from swagger_server.models.sign_up_response import SignUpResponse  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_info_response import UserInfoResponse  # noqa: E501
from swagger_server import util


def user_get_by_id(id):  # noqa: E501
    """user_get_by_id

    Get user info by ID # noqa: E501

    :param id: ID of a user
    :type id: dict | bytes

    :rtype: UserInfoResponse
    """
    return 'do some magic!'


def user_set_info(body):  # noqa: E501
    """Set users&#x27; info such as name, language, profile image etc.

    Set all fields to the current values, except for the overriden ones. No field should be missing. User ID must always be the ID of the current user.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SignUpResponse
    """
    if connexion.request.is_json:
        body = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_wait_for_partner():  # noqa: E501
    """user_wait_for_partner

    Wait for a match. # noqa: E501


    :rtype: PartnerResponse
    """
    return 'do some magic!'
