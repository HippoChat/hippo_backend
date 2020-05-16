import connexion
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from swagger_server.models import UserInfo, UserInfoSelf, UserInfoSelfPrivate
from swagger_server.models.age_group import AgeGroupEnum
from swagger_server.models.language_spec import LanguageSpecEnum
from swagger_server.models.response_base import ResponseBase  # noqa: E501
from swagger_server.models.sign_up_request import SignUpRequest  # noqa: E501
from swagger_server.models.sign_up_response import SignUpResponse  # noqa: E501
from swagger_server.models.user_id import UserId  # noqa: E501
from swagger_server.models.verification_code_request import VerificationCodeRequest  # noqa: E501
from swagger_server.models.verify_phone_code_request import VerifyPhoneCodeRequest  # noqa: E501
from swagger_server import util
from swagger_server.service import facebook, sms
from swagger_server.repository.auth import PendingVerification


def auth_send_verification_code(body):  # noqa: E501
    """auth_send_verification_code

    Send SMS with verification code # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if not connexion.request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    body = VerificationCodeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    v = sms.generate_verification_code(body.phone)
    sms.send_verification(v)
    return jsonify({"msg": "Verification code sent to your phone number"}), 200


def auth_verify_phone_code(body):  # noqa: E501
    """auth_verify_phone_code

    Verify the code sent via SMS # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: ResponseBase
    """
    if not connexion.request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    body = VerifyPhoneCodeRequest.from_dict(connexion.request.get_json())  # noqa: E501

    verified = sms.verify_code(phone=body.phone, code=body.code)
    if not verified:
        return jsonify({"msg": "Bad phone or verification code"}), 400

    return jsonify({"msg": "Phone number verified"}), 200


def auth_sign_up(body):  # noqa: E501
    """auth_sign_up

    Adds a new user to the system if they don’t exist yet # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: SignUpResponse
    """
    if not connexion.request.is_json:
        return SignUpResponse(status=400, error_message="Missing JSON in request"), 400

    body = SignUpRequest.from_dict(connexion.request.get_json())  # noqa: E501

    verified = sms.verify_code(phone=body.phone, code=body.code)
    if not verified:
        return SignUpResponse(status=400, error_message="Bad phone or verification code"), 400

    age_group = AgeGroupEnum(body.age_group)
    language = LanguageSpecEnum(body.language)

    user = facebook.register_user(phone=body.phone, name=body.name, age_group=age_group, language=language)

    cred = facebook.generate_credentials(user)

    user_info = facebook.get_user_info_self(cred)

    return SignUpResponse(status=200, me=user_info), 200


@jwt_required
def user_logout():  # noqa: E501
    """user_logout

    Logs a user out of the system # noqa: E501

    :rtype: ResponseBase
    """
    user = facebook.load_current_user()
    if user is None:
        return jsonify({"msg": "User not found"}), 400

    print(f"User logged out: #{user.id} @{user.name}")
    return jsonify({"msg": "Logged out"}), 200


def check_bearer_auth(token):
    return {}
