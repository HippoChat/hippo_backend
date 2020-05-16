from enum import Enum

AgeGroup = str


class AgeGroupEnum(Enum):
    """
    allowed enum values
    """
    G_18 = "<18"
    G_18_25 = "18-25"
    G_26_35 = "26-35"
    G_36_45 = "36-45"
    G_45 = ">45"
