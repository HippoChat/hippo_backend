from enum import Enum

AgeGroup = str


class AgeGroupEnum(Enum):
    """
    allowed enum values
    """
    _18 = "<18"
    _18_25 = "18-25"
    _26_35 = "26-35"
    _36_45 = "36-45"
    _45 = ">45"
