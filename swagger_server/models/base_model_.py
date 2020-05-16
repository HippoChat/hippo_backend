import pprint

import typing

from swagger_server import util

T = typing.TypeVar('T')


class Model(object):
    # swaggerTypes: The key is attribute name and the
    # value is attribute type.
    swagger_types = {}

    # attributeMap: The key is attribute name and the
    # value is json key in definition.
    attribute_map = {}

    @classmethod
    def from_dict(cls: typing.Type[T], dikt) -> T:
        """Returns the dict as a model"""
        return util.deserialize_model(dikt, cls)

    def to_dict(self):
        """Returns the model properties as a dict

        :rtype: dict
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = [
                    self.__to_dict_or_id(x)
                    for x in value
                ]
            elif callable(getattr(value, "to_dict", None)):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = {
                    k: self.__to_dict_or_id(v)
                    for (k, v) in value.items()
                }
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model

        :rtype: str
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    @staticmethod
    def __to_dict_or_id(v) -> object:
        if callable(getattr(v, "to_dict")):
            return v.to_dict()
        else:
            return v
