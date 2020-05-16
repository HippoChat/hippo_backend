from dataclasses import dataclass

from swagger_server.models import UserId


@dataclass
class PendingVerification:
    phone: str
    code: str


@dataclass
class UserCredentials:
    id: UserId
    token: str
