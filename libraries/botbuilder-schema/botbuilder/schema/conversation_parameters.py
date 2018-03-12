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


class ConversationParameters(Model):
    """Parameters for creating a new conversation.

    :param is_group: IsGroup
    :type is_group: bool
    :param bot: The bot address for this conversation
    :type bot: ~botframework.connector.models.ChannelAccount
    :param members: Members to add to the conversation
    :type members: list[~botframework.connector.models.ChannelAccount]
    :param topic_name: (Optional) Topic of the conversation (if supported by
     the channel)
    :type topic_name: str
    :param activity: (Optional) When creating a new conversation, use this
     activity as the intial message to the conversation
    :type activity: ~botframework.connector.models.Activity
    :param channel_data: Channel specific payload for creating the
     conversation
    :type channel_data: object
    """

    _attribute_map = {
        'is_group': {'key': 'isGroup', 'type': 'bool'},
        'bot': {'key': 'bot', 'type': 'ChannelAccount'},
        'members': {'key': 'members', 'type': '[ChannelAccount]'},
        'topic_name': {'key': 'topicName', 'type': 'str'},
        'activity': {'key': 'activity', 'type': 'Activity'},
        'channel_data': {'key': 'channelData', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ConversationParameters, self).__init__(**kwargs)
        self.is_group = kwargs.get('is_group', None)
        self.bot = kwargs.get('bot', None)
        self.members = kwargs.get('members', None)
        self.topic_name = kwargs.get('topic_name', None)
        self.activity = kwargs.get('activity', None)
        self.channel_data = kwargs.get('channel_data', None)
