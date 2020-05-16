from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from swagger_server.models import AgeGroup, LanguageSpec, Phone, SignUpRequest, UserId, UserInfo, UserInfoSelf, \
    UserInfoSelfPrivate
from swagger_server.models.age_group import AgeGroupEnum
from swagger_server.models.language_spec import LanguageSpecEnum
from swagger_server.repository.auth import UserCredentials
from swagger_server.repository.user import User
from typing import Dict, Optional

__registered_users: Dict[UserId, User] = {}
__last_id: int = 0  # last used UserId


def generate_new_user_id() -> UserId:
    global __last_id
    new_id = __last_id + 1
    __last_id += 1
    return UserId(new_id)


def register_user(
        phone: Phone,
        name: str,
        age_group: AgeGroupEnum,
        language: LanguageSpecEnum
) -> User:
    uid = generate_new_user_id()

    user = User(
        id=uid,
        name=name,
        age_group=age_group,
        language=language,
        image="",
        phone=phone,
    )

    save_user(user)

    return user


def load_user_by_id(user_id: UserId) -> Optional[User]:
    return __registered_users.get(user_id)


def load_current_user() -> Optional[User]:
    identity = get_jwt_identity()
    return load_user_by_id(identity)


def save_user(user: User) -> None:
    __registered_users[user.id] = user


def generate_credentials(user: User) -> UserCredentials:
    access_token = create_access_token(identity=user.id, expires_delta=False)
    return UserCredentials(id=user.id, token=access_token)


def get_user_info_self(cred: UserCredentials) -> UserInfoSelf:
    user = __registered_users[cred.id]
    return UserInfoSelf(
        public=get_user_info(user),
        private=UserInfoSelfPrivate(
            phone=user.phone,
            token=cred.token,
        )
    )


def get_user_info(user: User) -> UserInfo:
    return UserInfo(
        id=user.id,
        name=user.name,
        age_group=user.age_group.value,
        language=user.language.value,
        image=user.image,
    )


def patch(user: User, body: UserInfo):
    user.name = body.name
    user.image = body.image
    user.language = LanguageSpecEnum(body.language)
    user.age_group = AgeGroupEnum(body.age_group)
