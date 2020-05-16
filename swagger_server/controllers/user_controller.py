import connexion
from flask import jsonify
from flask_jwt_extended import jwt_required

from swagger_server.models import ResponseBase
from swagger_server.models.partner_response import PartnerResponse  # noqa: E501
from swagger_server.models.sign_up_response import SignUpResponse  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_info_response import UserInfoResponse  # noqa: E501
from swagger_server import util
from swagger_server.repository.auth import UserCredentials
from swagger_server.service import facebook


@jwt_required
def user_get_by_id(id_):  # noqa: E501
    """user_get_by_id

    Get user info by ID # noqa: E501

    :param id_: ID of a user
    :type id_: dict | bytes

    :rtype: UserInfoResponse
    """
    user_id = int(id_)
    user = facebook.load_user_by_id(user_id)
    if user is None:
        return ResponseBase(status=404, error_message="User not found"), 404

    user_info = facebook.get_user_info(user)

    return UserInfoResponse(status=200, user=user_info)


@jwt_required
def user_set_info(body):  # noqa: E501
    """Set users&#x27; info such as name, language, profile image etc.

    Set all fields to the current values, except for the overridden ones. No field should be missing. User ID must always be the ID of the current user.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SignUpResponse
    """
    if not connexion.request.is_json:
        return SignUpResponse(status=400, error_message="Missing JSON in request"), 400

    body = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    me = facebook.load_current_user()

    if me is None:
        return SignUpResponse(status=404, error_message="User not found"), 404

    if me.id != body.id:
        return SignUpResponse(status=400, error_message="ID does not match"), 400

    facebook.patch(me, body)
    facebook.save_user(me)

    cred = facebook.generate_credentials(me)
    user_info = facebook.get_user_info_self(cred)
    return SignUpResponse(status=200, me=user_info)


def user_wait_for_partner():  # noqa: E501
    """user_wait_for_partner

    Wait for a match. # noqa: E501


    :rtype: PartnerResponse
    """
    return 'do some magic!'
