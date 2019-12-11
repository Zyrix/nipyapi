# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.10.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ParameterContextUpdateRequestEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'parameter_context_revision': 'RevisionDTO',
        'request': 'ParameterContextUpdateRequestDTO'
    }

    attribute_map = {
        'parameter_context_revision': 'parameterContextRevision',
        'request': 'request'
    }

    def __init__(self, parameter_context_revision=None, request=None):
        """
        ParameterContextUpdateRequestEntity - a model defined in Swagger
        """

        self._parameter_context_revision = None
        self._request = None

        if parameter_context_revision is not None:
          self.parameter_context_revision = parameter_context_revision
        if request is not None:
          self.request = request

    @property
    def parameter_context_revision(self):
        """
        Gets the parameter_context_revision of this ParameterContextUpdateRequestEntity.
        The Revision of the Parameter Context

        :return: The parameter_context_revision of this ParameterContextUpdateRequestEntity.
        :rtype: RevisionDTO
        """
        return self._parameter_context_revision

    @parameter_context_revision.setter
    def parameter_context_revision(self, parameter_context_revision):
        """
        Sets the parameter_context_revision of this ParameterContextUpdateRequestEntity.
        The Revision of the Parameter Context

        :param parameter_context_revision: The parameter_context_revision of this ParameterContextUpdateRequestEntity.
        :type: RevisionDTO
        """

        self._parameter_context_revision = parameter_context_revision

    @property
    def request(self):
        """
        Gets the request of this ParameterContextUpdateRequestEntity.
        The Update Request

        :return: The request of this ParameterContextUpdateRequestEntity.
        :rtype: ParameterContextUpdateRequestDTO
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this ParameterContextUpdateRequestEntity.
        The Update Request

        :param request: The request of this ParameterContextUpdateRequestEntity.
        :type: ParameterContextUpdateRequestDTO
        """

        self._request = request

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ParameterContextUpdateRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other