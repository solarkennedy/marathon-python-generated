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


class V2appsContainerDockerPortMappings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V2appsContainerDockerPortMappings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'protocol': 'str',
            'container_port': 'int',
            'host_port': 'int',
            'service_port': 'int'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'container_port': 'containerPort',
            'host_port': 'hostPort',
            'service_port': 'servicePort'
        }

        self._protocol = None
        self._container_port = None
        self._host_port = None
        self._service_port = None

    @property
    def protocol(self):
        """
        Gets the protocol of this V2appsContainerDockerPortMappings.
        parameter is optional and defaults to tcp.

        :return: The protocol of this V2appsContainerDockerPortMappings.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V2appsContainerDockerPortMappings.
        parameter is optional and defaults to tcp.

        :param protocol: The protocol of this V2appsContainerDockerPortMappings.
        :type: str
        """
        self._protocol = protocol

    @property
    def container_port(self):
        """
        Gets the container_port of this V2appsContainerDockerPortMappings.
        Refers to the port the application listens to inside of the container. It is optional and now defaults to 0, in which case Marathon assigns the container port the same value as the assigned hostPort. This is especially useful for apps that advertise the port they are listening on to the outside world for P2P communication. Without containerPort: 0 they would erroneously advertise their private container port which is usually not the same as the externally visible host port.

        :return: The container_port of this V2appsContainerDockerPortMappings.
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        """
        Sets the container_port of this V2appsContainerDockerPortMappings.
        Refers to the port the application listens to inside of the container. It is optional and now defaults to 0, in which case Marathon assigns the container port the same value as the assigned hostPort. This is especially useful for apps that advertise the port they are listening on to the outside world for P2P communication. Without containerPort: 0 they would erroneously advertise their private container port which is usually not the same as the externally visible host port.

        :param container_port: The container_port of this V2appsContainerDockerPortMappings.
        :type: int
        """
        self._container_port = container_port

    @property
    def host_port(self):
        """
        Gets the host_port of this V2appsContainerDockerPortMappings.
        Retains the traditional meaning in Marathon, which is a random port from the range included in the Mesos resource offer. The resulting host ports for each task are exposed via the task details in the REST API and the Marathon web UI. hostPort is optional and defaults to 0.

        :return: The host_port of this V2appsContainerDockerPortMappings.
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        """
        Sets the host_port of this V2appsContainerDockerPortMappings.
        Retains the traditional meaning in Marathon, which is a random port from the range included in the Mesos resource offer. The resulting host ports for each task are exposed via the task details in the REST API and the Marathon web UI. hostPort is optional and defaults to 0.

        :param host_port: The host_port of this V2appsContainerDockerPortMappings.
        :type: int
        """
        self._host_port = host_port

    @property
    def service_port(self):
        """
        Gets the service_port of this V2appsContainerDockerPortMappings.
        Is a helper port intended for doing service discovery using a well-known port per service. The assigned servicePort value is not used/interpreted by Marathon itself but supposed to used by load balancer infrastructure. See Service Discovery Load Balancing doc page. The servicePort parameter is optional and defaults to 0. Like hostPort, If the value is 0, a random port will be assigned. If a servicePort value is assigned by Marathon then Marathon guarantees that its value is unique across the cluster. The values for random service ports are in the range [local_port_min, local_port_max] where local_port_min and local_port_max are command line options with default values of 10000 and 20000, respectively.

        :return: The service_port of this V2appsContainerDockerPortMappings.
        :rtype: int
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """
        Sets the service_port of this V2appsContainerDockerPortMappings.
        Is a helper port intended for doing service discovery using a well-known port per service. The assigned servicePort value is not used/interpreted by Marathon itself but supposed to used by load balancer infrastructure. See Service Discovery Load Balancing doc page. The servicePort parameter is optional and defaults to 0. Like hostPort, If the value is 0, a random port will be assigned. If a servicePort value is assigned by Marathon then Marathon guarantees that its value is unique across the cluster. The values for random service ports are in the range [local_port_min, local_port_max] where local_port_min and local_port_max are command line options with default values of 10000 and 20000, respectively.

        :param service_port: The service_port of this V2appsContainerDockerPortMappings.
        :type: int
        """
        self._service_port = service_port

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

