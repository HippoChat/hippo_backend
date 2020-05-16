from dataclasses import dataclass

from swagger_server.models import AgeGroup, Image, LanguageSpec, Phone, UserId
from swagger_server.models.age_group import AgeGroupEnum
from swagger_server.models.language_spec import LanguageSpecEnum


@dataclass
class User:
    id: UserId
    phone: Phone
    name: str
    age_group: AgeGroupEnum
    language: LanguageSpecEnum
    image: Image
