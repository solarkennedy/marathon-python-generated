# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Body2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Body2 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'PathType',
            'apps': 'list[AppDefinition1]',
            'groups': 'list[]',
            'dependencies': 'list[PathType]',
            'version': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'apps': 'apps',
            'groups': 'groups',
            'dependencies': 'dependencies',
            'version': 'version'
        }

        self._id = None
        self._apps = None
        self._groups = None
        self._dependencies = None
        self._version = None

    @property
    def id(self):
        """
        Gets the id of this Body2.
        Unique identifier for the app consisting of a series of names separated by slashes. Each name must be at least 1 character and may only contain digits (`0-9`), dashes (`-`), dots (`.`), and lowercase letters (`a-z`). The name may not begin or end with a dash.

        :return: The id of this Body2.
        :rtype: PathType
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Body2.
        Unique identifier for the app consisting of a series of names separated by slashes. Each name must be at least 1 character and may only contain digits (`0-9`), dashes (`-`), dots (`.`), and lowercase letters (`a-z`). The name may not begin or end with a dash.

        :param id: The id of this Body2.
        :type: PathType
        """
        self._id = id

    @property
    def apps(self):
        """
        Gets the apps of this Body2.
        The list of AppDefinitions in this group. See AppDefinition.json for the schema.

        :return: The apps of this Body2.
        :rtype: list[AppDefinition1]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """
        Sets the apps of this Body2.
        The list of AppDefinitions in this group. See AppDefinition.json for the schema.

        :param apps: The apps of this Body2.
        :type: list[AppDefinition1]
        """
        self._apps = apps

    @property
    def groups(self):
        """
        Gets the groups of this Body2.
        Groups can build a tree. Each group can contain sub-groups. The sub-groups are defined here.

        :return: The groups of this Body2.
        :rtype: list[]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this Body2.
        Groups can build a tree. Each group can contain sub-groups. The sub-groups are defined here.

        :param groups: The groups of this Body2.
        :type: list[]
        """
        self._groups = groups

    @property
    def dependencies(self):
        """
        Gets the dependencies of this Body2.
        A list of services upon which this application depends. An order is derived from the dependencies for performing start/stop and upgrade of the application. For example, an application /a relies on the services /b which itself relies on /c. To start all 3 applications, first /c is started than /b than /a.

        :return: The dependencies of this Body2.
        :rtype: list[PathType]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this Body2.
        A list of services upon which this application depends. An order is derived from the dependencies for performing start/stop and upgrade of the application. For example, an application /a relies on the services /b which itself relies on /c. To start all 3 applications, first /c is started than /b than /a.

        :param dependencies: The dependencies of this Body2.
        :type: list[PathType]
        """
        self._dependencies = dependencies

    @property
    def version(self):
        """
        Gets the version of this Body2.
        The version of this definition.

        :return: The version of this Body2.
        :rtype: datetime
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Body2.
        The version of this definition.

        :param version: The version of this Body2.
        :type: datetime
        """
        self._version = version

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

