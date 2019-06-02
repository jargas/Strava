# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Error(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'field': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'code': 'code',
        'field': 'field',
        'resource': 'resource'
    }

    def __init__(self, code=None, field=None, resource=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._field = None
        self._resource = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if field is not None:
            self.field = field
        if resource is not None:
            self.resource = resource

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501

        The code associated with this error.  # noqa: E501

        :return: The code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.

        The code associated with this error.  # noqa: E501

        :param code: The code of this Error.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def field(self):
        """Gets the field of this Error.  # noqa: E501

        The specific field or aspect of the resource associated with this error.  # noqa: E501

        :return: The field of this Error.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Error.

        The specific field or aspect of the resource associated with this error.  # noqa: E501

        :param field: The field of this Error.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def resource(self):
        """Gets the resource of this Error.  # noqa: E501

        The type of resource associated with this error.  # noqa: E501

        :return: The resource of this Error.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Error.

        The type of resource associated with this error.  # noqa: E501

        :param resource: The resource of this Error.  # noqa: E501
        :type: str
        """

        self._resource = resource

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Error, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
