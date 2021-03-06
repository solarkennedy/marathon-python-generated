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


class HealthCheck(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HealthCheck - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'command': 'list[Command]',
            'grace_period_seconds': 'int',
            'ignore_http1xx': 'bool',
            'interval_seconds': 'int',
            'max_consecutive_failures': 'int',
            'path': 'str',
            'port': 'int',
            'port_index': 'int',
            'protocol': 'Protocol',
            'timeout_seconds': 'int'
        }

        self.attribute_map = {
            'command': 'command',
            'grace_period_seconds': 'gracePeriodSeconds',
            'ignore_http1xx': 'ignoreHttp1xx',
            'interval_seconds': 'intervalSeconds',
            'max_consecutive_failures': 'maxConsecutiveFailures',
            'path': 'path',
            'port': 'port',
            'port_index': 'portIndex',
            'protocol': 'protocol',
            'timeout_seconds': 'timeoutSeconds'
        }

        self._command = None
        self._grace_period_seconds = None
        self._ignore_http1xx = None
        self._interval_seconds = None
        self._max_consecutive_failures = None
        self._path = None
        self._port = None
        self._port_index = None
        self._protocol = None
        self._timeout_seconds = None

    @property
    def command(self):
        """
        Gets the command of this HealthCheck.


        :return: The command of this HealthCheck.
        :rtype: list[Command]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this HealthCheck.


        :param command: The command of this HealthCheck.
        :type: list[Command]
        """
        self._command = command

    @property
    def grace_period_seconds(self):
        """
        Gets the grace_period_seconds of this HealthCheck.
        Health check failures are ignored within this number of seconds of the task being started or until the task becomes healthy for the first time.

        :return: The grace_period_seconds of this HealthCheck.
        :rtype: int
        """
        return self._grace_period_seconds

    @grace_period_seconds.setter
    def grace_period_seconds(self, grace_period_seconds):
        """
        Sets the grace_period_seconds of this HealthCheck.
        Health check failures are ignored within this number of seconds of the task being started or until the task becomes healthy for the first time.

        :param grace_period_seconds: The grace_period_seconds of this HealthCheck.
        :type: int
        """
        self._grace_period_seconds = grace_period_seconds

    @property
    def ignore_http1xx(self):
        """
        Gets the ignore_http1xx of this HealthCheck.
        Ignore HTTP 1xx responses.

        :return: The ignore_http1xx of this HealthCheck.
        :rtype: bool
        """
        return self._ignore_http1xx

    @ignore_http1xx.setter
    def ignore_http1xx(self, ignore_http1xx):
        """
        Sets the ignore_http1xx of this HealthCheck.
        Ignore HTTP 1xx responses.

        :param ignore_http1xx: The ignore_http1xx of this HealthCheck.
        :type: bool
        """
        self._ignore_http1xx = ignore_http1xx

    @property
    def interval_seconds(self):
        """
        Gets the interval_seconds of this HealthCheck.
        Number of seconds to wait between health checks.

        :return: The interval_seconds of this HealthCheck.
        :rtype: int
        """
        return self._interval_seconds

    @interval_seconds.setter
    def interval_seconds(self, interval_seconds):
        """
        Sets the interval_seconds of this HealthCheck.
        Number of seconds to wait between health checks.

        :param interval_seconds: The interval_seconds of this HealthCheck.
        :type: int
        """
        self._interval_seconds = interval_seconds

    @property
    def max_consecutive_failures(self):
        """
        Gets the max_consecutive_failures of this HealthCheck.
        Number of consecutive health check failures after which the unhealthy task should be killed.

        :return: The max_consecutive_failures of this HealthCheck.
        :rtype: int
        """
        return self._max_consecutive_failures

    @max_consecutive_failures.setter
    def max_consecutive_failures(self, max_consecutive_failures):
        """
        Sets the max_consecutive_failures of this HealthCheck.
        Number of consecutive health check failures after which the unhealthy task should be killed.

        :param max_consecutive_failures: The max_consecutive_failures of this HealthCheck.
        :type: int
        """
        self._max_consecutive_failures = max_consecutive_failures

    @property
    def path(self):
        """
        Gets the path of this HealthCheck.
        Path to endpoint exposed by the task that will provide health status. Example: /path/to/health. Note: only used if protocol == HTTP[S].

        :return: The path of this HealthCheck.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this HealthCheck.
        Path to endpoint exposed by the task that will provide health status. Example: /path/to/health. Note: only used if protocol == HTTP[S].

        :param path: The path of this HealthCheck.
        :type: str
        """
        self._path = path

    @property
    def port(self):
        """
        Gets the port of this HealthCheck.
        The specific port to connect to. In case of dynamic ports, see portIndex.

        :return: The port of this HealthCheck.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this HealthCheck.
        The specific port to connect to. In case of dynamic ports, see portIndex.

        :param port: The port of this HealthCheck.
        :type: int
        """
        self._port = port

    @property
    def port_index(self):
        """
        Gets the port_index of this HealthCheck.
        Index in this app's ports array to be used for health requests. An index is used so the app can use random ports, like [0, 0, 0] for example, and tasks could be started with port environment variables like $PORT1.

        :return: The port_index of this HealthCheck.
        :rtype: int
        """
        return self._port_index

    @port_index.setter
    def port_index(self, port_index):
        """
        Sets the port_index of this HealthCheck.
        Index in this app's ports array to be used for health requests. An index is used so the app can use random ports, like [0, 0, 0] for example, and tasks could be started with port environment variables like $PORT1.

        :param port_index: The port_index of this HealthCheck.
        :type: int
        """
        self._port_index = port_index

    @property
    def protocol(self):
        """
        Gets the protocol of this HealthCheck.
        Protocol of the requests to be performed. One of HTTP, HTTPS, TCP or COMMAND.

        :return: The protocol of this HealthCheck.
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this HealthCheck.
        Protocol of the requests to be performed. One of HTTP, HTTPS, TCP or COMMAND.

        :param protocol: The protocol of this HealthCheck.
        :type: Protocol
        """
        self._protocol = protocol

    @property
    def timeout_seconds(self):
        """
        Gets the timeout_seconds of this HealthCheck.
        Number of seconds after which a health check is considered a failure regardless of the response.

        :return: The timeout_seconds of this HealthCheck.
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """
        Sets the timeout_seconds of this HealthCheck.
        Number of seconds after which a health check is considered a failure regardless of the response.

        :param timeout_seconds: The timeout_seconds of this HealthCheck.
        :type: int
        """
        self._timeout_seconds = timeout_seconds

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

