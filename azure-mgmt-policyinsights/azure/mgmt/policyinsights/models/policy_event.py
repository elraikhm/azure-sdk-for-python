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

from msrest.serialization import Model


class PolicyEvent(Model):
    """Policy event record.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param odataid: OData entity ID; always set to null since policy event
     records do not have an entity ID.
    :type odataid: str
    :param odatacontext: OData context string; used by OData clients to
     resolve type information based on metadata.
    :type odatacontext: str
    :param timestamp: Timestamp for the policy event record.
    :type timestamp: datetime
    :param resource_id: Resource ID.
    :type resource_id: str
    :param policy_assignment_id: Policy assignment ID.
    :type policy_assignment_id: str
    :param policy_definition_id: Policy definition ID.
    :type policy_definition_id: str
    :param effective_parameters: Effective parameters for the policy
     assignment.
    :type effective_parameters: str
    :param is_compliant: Flag which states whether the resource is compliant
     against the policy assignment it was evaluated against.
    :type is_compliant: bool
    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param resource_type: Resource type.
    :type resource_type: str
    :param resource_location: Resource location.
    :type resource_location: str
    :param resource_group: Resource group name.
    :type resource_group: str
    :param resource_tags: List of resource tags.
    :type resource_tags: str
    :param policy_assignment_name: Policy assignment name.
    :type policy_assignment_name: str
    :param policy_assignment_owner: Policy assignment owner.
    :type policy_assignment_owner: str
    :param policy_assignment_parameters: Policy assignment parameters.
    :type policy_assignment_parameters: str
    :param policy_assignment_scope: Policy assignment scope.
    :type policy_assignment_scope: str
    :param policy_definition_name: Policy definition name.
    :type policy_definition_name: str
    :param policy_definition_action: Policy definition action, i.e. effect.
    :type policy_definition_action: str
    :param policy_definition_category: Policy definition category.
    :type policy_definition_category: str
    :param policy_set_definition_id: Policy set definition ID, if the policy
     assignment is for a policy set.
    :type policy_set_definition_id: str
    :param policy_set_definition_name: Policy set definition name, if the
     policy assignment is for a policy set.
    :type policy_set_definition_name: str
    :param policy_set_definition_owner: Policy set definition owner, if the
     policy assignment is for a policy set.
    :type policy_set_definition_owner: str
    :param policy_set_definition_category: Policy set definition category, if
     the policy assignment is for a policy set.
    :type policy_set_definition_category: str
    :param policy_set_definition_parameters: Policy set definition parameters,
     if the policy assignment is for a policy set.
    :type policy_set_definition_parameters: str
    :param management_group_ids: Comma separated list of management group IDs,
     which represent the hierarchy of the management groups the resource is
     under.
    :type management_group_ids: str
    :param policy_definition_reference_id: Reference ID for the policy
     definition inside the policy set, if the policy assignment is for a policy
     set.
    :type policy_definition_reference_id: str
    :param tenant_id: Tenant ID for the policy event record.
    :type tenant_id: str
    :param principal_oid: Principal object ID for the user who initiated the
     resource operation that triggered the policy event.
    :type principal_oid: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'odataid': {'key': '@odata\\.id', 'type': 'str'},
        'odatacontext': {'key': '@odata\\.context', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'policy_assignment_id': {'key': 'policyAssignmentId', 'type': 'str'},
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
        'effective_parameters': {'key': 'effectiveParameters', 'type': 'str'},
        'is_compliant': {'key': 'isCompliant', 'type': 'bool'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'resource_tags': {'key': 'resourceTags', 'type': 'str'},
        'policy_assignment_name': {'key': 'policyAssignmentName', 'type': 'str'},
        'policy_assignment_owner': {'key': 'policyAssignmentOwner', 'type': 'str'},
        'policy_assignment_parameters': {'key': 'policyAssignmentParameters', 'type': 'str'},
        'policy_assignment_scope': {'key': 'policyAssignmentScope', 'type': 'str'},
        'policy_definition_name': {'key': 'policyDefinitionName', 'type': 'str'},
        'policy_definition_action': {'key': 'policyDefinitionAction', 'type': 'str'},
        'policy_definition_category': {'key': 'policyDefinitionCategory', 'type': 'str'},
        'policy_set_definition_id': {'key': 'policySetDefinitionId', 'type': 'str'},
        'policy_set_definition_name': {'key': 'policySetDefinitionName', 'type': 'str'},
        'policy_set_definition_owner': {'key': 'policySetDefinitionOwner', 'type': 'str'},
        'policy_set_definition_category': {'key': 'policySetDefinitionCategory', 'type': 'str'},
        'policy_set_definition_parameters': {'key': 'policySetDefinitionParameters', 'type': 'str'},
        'management_group_ids': {'key': 'managementGroupIds', 'type': 'str'},
        'policy_definition_reference_id': {'key': 'policyDefinitionReferenceId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'principal_oid': {'key': 'principalOid', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicyEvent, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.odataid = kwargs.get('odataid', None)
        self.odatacontext = kwargs.get('odatacontext', None)
        self.timestamp = kwargs.get('timestamp', None)
        self.resource_id = kwargs.get('resource_id', None)
        self.policy_assignment_id = kwargs.get('policy_assignment_id', None)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.effective_parameters = kwargs.get('effective_parameters', None)
        self.is_compliant = kwargs.get('is_compliant', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.resource_type = kwargs.get('resource_type', None)
        self.resource_location = kwargs.get('resource_location', None)
        self.resource_group = kwargs.get('resource_group', None)
        self.resource_tags = kwargs.get('resource_tags', None)
        self.policy_assignment_name = kwargs.get('policy_assignment_name', None)
        self.policy_assignment_owner = kwargs.get('policy_assignment_owner', None)
        self.policy_assignment_parameters = kwargs.get('policy_assignment_parameters', None)
        self.policy_assignment_scope = kwargs.get('policy_assignment_scope', None)
        self.policy_definition_name = kwargs.get('policy_definition_name', None)
        self.policy_definition_action = kwargs.get('policy_definition_action', None)
        self.policy_definition_category = kwargs.get('policy_definition_category', None)
        self.policy_set_definition_id = kwargs.get('policy_set_definition_id', None)
        self.policy_set_definition_name = kwargs.get('policy_set_definition_name', None)
        self.policy_set_definition_owner = kwargs.get('policy_set_definition_owner', None)
        self.policy_set_definition_category = kwargs.get('policy_set_definition_category', None)
        self.policy_set_definition_parameters = kwargs.get('policy_set_definition_parameters', None)
        self.management_group_ids = kwargs.get('management_group_ids', None)
        self.policy_definition_reference_id = kwargs.get('policy_definition_reference_id', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.principal_oid = kwargs.get('principal_oid', None)