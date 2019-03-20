# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.models.base_model_ import Model
from api.models.item_affected import ItemsAffected
from api import util


class AgentGroupDeleted(Model):

    def __init__(self, item_affected: ItemsAffected=None, affected_agents: List[str]=None):
        """AgentGroupDeleted body model
        :param item_affected: The item_affected of this AgentGroupDeleted.
        :type item_affected: ItemsAffected
        :param affected_agents: List of agents which belonged to the group but were moved to the default one.
        :type affected_agents: List[str]
        """
        self.swagger_types = {
            'item_affected': ItemsAffected,
            'affected_agents': List[str]
        }

        self.attribute_map = {
            'item_affected': item_affected,
            'affected_agents': affected_agents
        }

        self._item_affected = item_affected
        self._affected_agents = affected_agents

    @classmethod
    def from_dict(cls, dikt) -> AgentGroupDeleted:
        """Returns the dict as a model
        :param dikt: A dict.
        :type: dict
        :return: The AgentGroupDeleted of this AgentGroupDeleted.
        :rtype: dict
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item_affected(self) -> ItemsAffected:
        """
        :return: The item_affected of this AgentGroupDeleted
        :rtype: ItemsAffected
        """
        return self._item_affected

    @item_affected.setter
    def item_affected(self, item_affected):
        """
        :param item_affected: The item_affected of this AgentGroupDeleted.
        """
        self._item_affected = item_affected

    @property
    def affected_agents(self) -> List[str]:
        """
        :return: The affected_agents of this AgentGroupDeleted
        :rtype: List[str]
        """
        return self._affected_agents

    @affected_agents.setter
    def affected_agents(self, affected_agents):
        """
        :param affected_agents: The affected_agents of this AgentGroupDeleted.
        """
        self._affected_agents = affected_agents