# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NPC(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, race: str=None, _class: str=None, alignment: str=None, languages: List[str]=None, special_abilities: List[str]=None):  # noqa: E501
        """NPC - a model defined in Swagger

        :param name: The name of this NPC.  # noqa: E501
        :type name: str
        :param race: The race of this NPC.  # noqa: E501
        :type race: str
        :param _class: The _class of this NPC.  # noqa: E501
        :type _class: str
        :param alignment: The alignment of this NPC.  # noqa: E501
        :type alignment: str
        :param languages: The languages of this NPC.  # noqa: E501
        :type languages: List[str]
        :param special_abilities: The special_abilities of this NPC.  # noqa: E501
        :type special_abilities: List[str]
        """
        self.swagger_types = {
            'name': str,
            'race': str,
            '_class': str,
            'alignment': str,
            'languages': List[str],
            'special_abilities': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'race': 'race',
            '_class': 'class',
            'alignment': 'alignment',
            'languages': 'languages',
            'special_abilities': 'specialAbilities'
        }
        self._name = name
        self._race = race
        self.__class = _class
        self._alignment = alignment
        self._languages = languages
        self._special_abilities = special_abilities

    @classmethod
    def from_dict(cls, dikt) -> 'NPC':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NPC of this NPC.  # noqa: E501
        :rtype: NPC
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this NPC.


        :return: The name of this NPC.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this NPC.


        :param name: The name of this NPC.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def race(self) -> str:
        """Gets the race of this NPC.


        :return: The race of this NPC.
        :rtype: str
        """
        return self._race

    @race.setter
    def race(self, race: str):
        """Sets the race of this NPC.


        :param race: The race of this NPC.
        :type race: str
        """
        if race is None:
            raise ValueError("Invalid value for `race`, must not be `None`")  # noqa: E501

        self._race = race

    @property
    def _class(self) -> str:
        """Gets the _class of this NPC.


        :return: The _class of this NPC.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class: str):
        """Sets the _class of this NPC.


        :param _class: The _class of this NPC.
        :type _class: str
        """

        self.__class = _class

    @property
    def alignment(self) -> str:
        """Gets the alignment of this NPC.


        :return: The alignment of this NPC.
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment: str):
        """Sets the alignment of this NPC.


        :param alignment: The alignment of this NPC.
        :type alignment: str
        """

        self._alignment = alignment

    @property
    def languages(self) -> List[str]:
        """Gets the languages of this NPC.


        :return: The languages of this NPC.
        :rtype: List[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages: List[str]):
        """Sets the languages of this NPC.


        :param languages: The languages of this NPC.
        :type languages: List[str]
        """

        self._languages = languages

    @property
    def special_abilities(self) -> List[str]:
        """Gets the special_abilities of this NPC.


        :return: The special_abilities of this NPC.
        :rtype: List[str]
        """
        return self._special_abilities

    @special_abilities.setter
    def special_abilities(self, special_abilities: List[str]):
        """Sets the special_abilities of this NPC.


        :param special_abilities: The special_abilities of this NPC.
        :type special_abilities: List[str]
        """

        self._special_abilities = special_abilities
