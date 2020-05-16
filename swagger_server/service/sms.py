from dataclasses import dataclass
from typing import Dict
import random

from swagger_server.repository.auth import PendingVerification

__pending_verifications_database: Dict[str, PendingVerification] = {}


def generate_verification_code(phone: str) -> PendingVerification:
    digit = lambda: random.randint(0, 9)
    code = "".join(str(digit()) for _ in range(4))
    v = PendingVerification(phone, code)
    return v


def send_verification(v: PendingVerification):
    __pending_verifications_database[v.phone] = v
    print(f"Send verification code: {v}")


def verify_code(phone: str, code: str) -> bool:
    v = __pending_verifications_database.get(phone, None)

    if v is None:
        return False

    if v.code != code:
        return False

    return True


def verification_finish(v: PendingVerification):
    __pending_verifications_database.pop(v.phone, None)
