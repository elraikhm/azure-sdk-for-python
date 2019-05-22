# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class ServiceUnitResource(TrackedResource):
    """Represents the response of a service unit resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param target_resource_group: Required. The Azure Resource Group to which
     the resources in the service unit belong to or should be deployed to.
    :type target_resource_group: str
    :param deployment_mode: Required. Describes the type of ARM deployment to
     be performed on the resource. Possible values include: 'Incremental',
     'Complete'
    :type deployment_mode: str or
     ~azure.mgmt.deploymentmanager.models.DeploymentMode
    :param artifacts: The artifacts for the service unit.
    :type artifacts: ~azure.mgmt.deploymentmanager.models.ServiceUnitArtifacts
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'target_resource_group': {'required': True},
        'deployment_mode': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'target_resource_group': {'key': 'properties.targetResourceGroup', 'type': 'str'},
        'deployment_mode': {'key': 'properties.deploymentMode', 'type': 'DeploymentMode'},
        'artifacts': {'key': 'properties.artifacts', 'type': 'ServiceUnitArtifacts'},
    }

    def __init__(self, *, location: str, target_resource_group: str, deployment_mode, tags=None, artifacts=None, **kwargs) -> None:
        super(ServiceUnitResource, self).__init__(tags=tags, location=location, **kwargs)
        self.target_resource_group = target_resource_group
        self.deployment_mode = deployment_mode
        self.artifacts = artifacts