from swagger_server.models import AgeGroup, Image, LanguageSpec, Phone, UserId
from swagger_server.models.age_group import AgeGroupEnum
from swagger_server.models.language_spec import LanguageSpecEnum
from swagger_server.repository.user import User

import random
from typing import List, Optional, Tuple

u1 = User(id=1, age_group=AgeGroupEnum.G_18, language=LanguageSpecEnum.RU_RU, image="", name="1", phone="")  # our user

u2 = User(id=2, age_group=AgeGroupEnum.G_18_25, language=LanguageSpecEnum.RU_RU, image="", name="2", phone="")
u3 = User(id=3, age_group=AgeGroupEnum.G_26_35, language=LanguageSpecEnum.EN_US, image="", name="3", phone="")
u4 = User(id=4, age_group=AgeGroupEnum.G_36_45, language=LanguageSpecEnum.FR_FR, image="", name="4", phone="")

partners = [u2, u3, u4]

Score = int


def age_to_scale(age: AgeGroupEnum) -> Score:
    scale = {
        AgeGroupEnum.G_18: 1,
        AgeGroupEnum.G_18_25: 2,
        AgeGroupEnum.G_26_35: 3,
        AgeGroupEnum.G_36_45: 4,
        AgeGroupEnum.G_45: 5,
    }
    return scale[age]


def age_score(lhs: AgeGroupEnum, rhs: AgeGroupEnum) -> Score:
    """
    :return: Score in range 0..4
    """
    lhs_scale = age_to_scale(lhs)
    rhs_scale = age_to_scale(rhs)
    return abs(lhs_scale - rhs_scale)


def language_score(lhs: LanguageSpecEnum, rhs: LanguageSpecEnum) -> Score:
    """
    :return: Score in range 0..3
    """
    if lhs == rhs:
        return 0
    else:
        return 3


BEST_SCORE: Score = age_score(AgeGroupEnum.G_18, AgeGroupEnum.G_18) \
                    + language_score(LanguageSpecEnum.RU_RU, LanguageSpecEnum.RU_RU)

WORST_SCORE: Score = age_score(AgeGroupEnum.G_18, AgeGroupEnum.G_45) \
                     + language_score(LanguageSpecEnum.RU_RU, LanguageSpecEnum.EN_US)


def match_users(user: User, online: List[User]) -> Optional[Tuple[User, Score]]:
    """
    Match users based on heuristic score. The less the score -- the better.

    :param user: current user
    :param online: other users
    :return:
    """
    online = [u for u in online if u.id != user.id]  # sanity check

    if len(online) == 0:
        return None

    scores = [0] * len(online)
    for i in range(len(online)):
        scores[i] += age_score(user.age_group, online[i].age_group)
        scores[i] += language_score(user.language, online[i].language)

    best_score = min(scores)
    bestest = [idx for idx, score in enumerate(scores) if score == best_score]

    assert len(bestest) != 0, "should never happen"
    lucky_idx = random.choice(bestest)

    lucky_user = online[lucky_idx]
    return lucky_user, best_score


print(match_users(u1, partners))
