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


class Entity(Model):
    """Object of schema.org types.

    :param type: Entity Type (typically from schema.org types)
    :type type: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, type: str=None, **kwargs) -> None:
        super(Entity, self).__init__(**kwargs)
        self.type = type
