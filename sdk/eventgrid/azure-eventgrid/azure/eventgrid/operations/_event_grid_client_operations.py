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

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from .. import models


class EventGridClientOperationsMixin(object):

    def publish_events(
            self, topic_hostname, events, custom_headers=None, raw=False, **operation_config):
        """Publishes a batch of events to an Azure Event Grid topic.

        :param topic_hostname: The host name of the topic, e.g.
         topic1.westus2-1.eventgrid.azure.net
        :type topic_hostname: str
        :param events: An array of events to be published to Event Grid.
        :type events: list[~azure.eventgrid.models.EventGridEvent]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        api_version = "2018-01-01"

        # Construct URL
        url = self.publish_events.metadata['url']
        path_format_arguments = {
            'topicHostname': self._serialize.url("topic_hostname", topic_hostname, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(events, '[EventGridEvent]')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    publish_events.metadata = {'url': '/api/events'}
