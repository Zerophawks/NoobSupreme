# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Item(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, type: str=None, rarity: str=None, description: str=None, properties: List[str]=None, attunement_required: bool=None, effect: str=None):  # noqa: E501
        """Item - a model defined in Swagger

        :param name: The name of this Item.  # noqa: E501
        :type name: str
        :param type: The type of this Item.  # noqa: E501
        :type type: str
        :param rarity: The rarity of this Item.  # noqa: E501
        :type rarity: str
        :param description: The description of this Item.  # noqa: E501
        :type description: str
        :param properties: The properties of this Item.  # noqa: E501
        :type properties: List[str]
        :param attunement_required: The attunement_required of this Item.  # noqa: E501
        :type attunement_required: bool
        :param effect: The effect of this Item.  # noqa: E501
        :type effect: str
        """
        self.swagger_types = {
            'name': str,
            'type': str,
            'rarity': str,
            'description': str,
            'properties': List[str],
            'attunement_required': bool,
            'effect': str
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'rarity': 'rarity',
            'description': 'description',
            'properties': 'properties',
            'attunement_required': 'attunementRequired',
            'effect': 'effect'
        }
        self._name = name
        self._type = type
        self._rarity = rarity
        self._description = description
        self._properties = properties
        self._attunement_required = attunement_required
        self._effect = effect

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Item.


        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Item.


        :param name: The name of this Item.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this Item.


        :return: The type of this Item.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Item.


        :param type: The type of this Item.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def rarity(self) -> str:
        """Gets the rarity of this Item.


        :return: The rarity of this Item.
        :rtype: str
        """
        return self._rarity

    @rarity.setter
    def rarity(self, rarity: str):
        """Sets the rarity of this Item.


        :param rarity: The rarity of this Item.
        :type rarity: str
        """
        if rarity is None:
            raise ValueError("Invalid value for `rarity`, must not be `None`")  # noqa: E501

        self._rarity = rarity

    @property
    def description(self) -> str:
        """Gets the description of this Item.


        :return: The description of this Item.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Item.


        :param description: The description of this Item.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def properties(self) -> List[str]:
        """Gets the properties of this Item.


        :return: The properties of this Item.
        :rtype: List[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: List[str]):
        """Sets the properties of this Item.


        :param properties: The properties of this Item.
        :type properties: List[str]
        """

        self._properties = properties

    @property
    def attunement_required(self) -> bool:
        """Gets the attunement_required of this Item.


        :return: The attunement_required of this Item.
        :rtype: bool
        """
        return self._attunement_required

    @attunement_required.setter
    def attunement_required(self, attunement_required: bool):
        """Sets the attunement_required of this Item.


        :param attunement_required: The attunement_required of this Item.
        :type attunement_required: bool
        """

        self._attunement_required = attunement_required

    @property
    def effect(self) -> str:
        """Gets the effect of this Item.


        :return: The effect of this Item.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect: str):
        """Sets the effect of this Item.


        :param effect: The effect of this Item.
        :type effect: str
        """

        self._effect = effect