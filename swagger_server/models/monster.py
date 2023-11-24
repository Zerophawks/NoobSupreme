# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.monster_ability_scores import MonsterAbilityScores  # noqa: F401,E501
from swagger_server import util


class Monster(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, type: str=None, size: str=None, alignment: str=None, ability_scores: MonsterAbilityScores=None, hit_points: int=None, speed: str=None, armor_class: int=None, skills: List[str]=None, senses: List[str]=None, languages: List[str]=None, challenge_rating: int=None, xp: int=None, special_abilities: List[str]=None, actions: List[str]=None, reactions: List[str]=None):  # noqa: E501
        """Monster - a model defined in Swagger

        :param name: The name of this Monster.  # noqa: E501
        :type name: str
        :param type: The type of this Monster.  # noqa: E501
        :type type: str
        :param size: The size of this Monster.  # noqa: E501
        :type size: str
        :param alignment: The alignment of this Monster.  # noqa: E501
        :type alignment: str
        :param ability_scores: The ability_scores of this Monster.  # noqa: E501
        :type ability_scores: MonsterAbilityScores
        :param hit_points: The hit_points of this Monster.  # noqa: E501
        :type hit_points: int
        :param speed: The speed of this Monster.  # noqa: E501
        :type speed: str
        :param armor_class: The armor_class of this Monster.  # noqa: E501
        :type armor_class: int
        :param skills: The skills of this Monster.  # noqa: E501
        :type skills: List[str]
        :param senses: The senses of this Monster.  # noqa: E501
        :type senses: List[str]
        :param languages: The languages of this Monster.  # noqa: E501
        :type languages: List[str]
        :param challenge_rating: The challenge_rating of this Monster.  # noqa: E501
        :type challenge_rating: int
        :param xp: The xp of this Monster.  # noqa: E501
        :type xp: int
        :param special_abilities: The special_abilities of this Monster.  # noqa: E501
        :type special_abilities: List[str]
        :param actions: The actions of this Monster.  # noqa: E501
        :type actions: List[str]
        :param reactions: The reactions of this Monster.  # noqa: E501
        :type reactions: List[str]
        """
        self.swagger_types = {
            'name': str,
            'type': str,
            'size': str,
            'alignment': str,
            'ability_scores': MonsterAbilityScores,
            'hit_points': int,
            'speed': str,
            'armor_class': int,
            'skills': List[str],
            'senses': List[str],
            'languages': List[str],
            'challenge_rating': int,
            'xp': int,
            'special_abilities': List[str],
            'actions': List[str],
            'reactions': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'size': 'size',
            'alignment': 'alignment',
            'ability_scores': 'abilityScores',
            'hit_points': 'hitPoints',
            'speed': 'speed',
            'armor_class': 'armorClass',
            'skills': 'skills',
            'senses': 'senses',
            'languages': 'languages',
            'challenge_rating': 'challengeRating',
            'xp': 'xp',
            'special_abilities': 'specialAbilities',
            'actions': 'actions',
            'reactions': 'reactions'
        }
        self._name = name
        self._type = type
        self._size = size
        self._alignment = alignment
        self._ability_scores = ability_scores
        self._hit_points = hit_points
        self._speed = speed
        self._armor_class = armor_class
        self._skills = skills
        self._senses = senses
        self._languages = languages
        self._challenge_rating = challenge_rating
        self._xp = xp
        self._special_abilities = special_abilities
        self._actions = actions
        self._reactions = reactions

    @classmethod
    def from_dict(cls, dikt) -> 'Monster':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Monster of this Monster.  # noqa: E501
        :rtype: Monster
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Monster.


        :return: The name of this Monster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Monster.


        :param name: The name of this Monster.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this Monster.


        :return: The type of this Monster.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Monster.


        :param type: The type of this Monster.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def size(self) -> str:
        """Gets the size of this Monster.


        :return: The size of this Monster.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size: str):
        """Sets the size of this Monster.


        :param size: The size of this Monster.
        :type size: str
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def alignment(self) -> str:
        """Gets the alignment of this Monster.


        :return: The alignment of this Monster.
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment: str):
        """Sets the alignment of this Monster.


        :param alignment: The alignment of this Monster.
        :type alignment: str
        """

        self._alignment = alignment

    @property
    def ability_scores(self) -> MonsterAbilityScores:
        """Gets the ability_scores of this Monster.


        :return: The ability_scores of this Monster.
        :rtype: MonsterAbilityScores
        """
        return self._ability_scores

    @ability_scores.setter
    def ability_scores(self, ability_scores: MonsterAbilityScores):
        """Sets the ability_scores of this Monster.


        :param ability_scores: The ability_scores of this Monster.
        :type ability_scores: MonsterAbilityScores
        """
        if ability_scores is None:
            raise ValueError("Invalid value for `ability_scores`, must not be `None`")  # noqa: E501

        self._ability_scores = ability_scores

    @property
    def hit_points(self) -> int:
        """Gets the hit_points of this Monster.


        :return: The hit_points of this Monster.
        :rtype: int
        """
        return self._hit_points

    @hit_points.setter
    def hit_points(self, hit_points: int):
        """Sets the hit_points of this Monster.


        :param hit_points: The hit_points of this Monster.
        :type hit_points: int
        """
        if hit_points is None:
            raise ValueError("Invalid value for `hit_points`, must not be `None`")  # noqa: E501

        self._hit_points = hit_points

    @property
    def speed(self) -> str:
        """Gets the speed of this Monster.


        :return: The speed of this Monster.
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed: str):
        """Sets the speed of this Monster.


        :param speed: The speed of this Monster.
        :type speed: str
        """

        self._speed = speed

    @property
    def armor_class(self) -> int:
        """Gets the armor_class of this Monster.


        :return: The armor_class of this Monster.
        :rtype: int
        """
        return self._armor_class

    @armor_class.setter
    def armor_class(self, armor_class: int):
        """Sets the armor_class of this Monster.


        :param armor_class: The armor_class of this Monster.
        :type armor_class: int
        """
        if armor_class is None:
            raise ValueError("Invalid value for `armor_class`, must not be `None`")  # noqa: E501

        self._armor_class = armor_class

    @property
    def skills(self) -> List[str]:
        """Gets the skills of this Monster.


        :return: The skills of this Monster.
        :rtype: List[str]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List[str]):
        """Sets the skills of this Monster.


        :param skills: The skills of this Monster.
        :type skills: List[str]
        """

        self._skills = skills

    @property
    def senses(self) -> List[str]:
        """Gets the senses of this Monster.


        :return: The senses of this Monster.
        :rtype: List[str]
        """
        return self._senses

    @senses.setter
    def senses(self, senses: List[str]):
        """Sets the senses of this Monster.


        :param senses: The senses of this Monster.
        :type senses: List[str]
        """

        self._senses = senses

    @property
    def languages(self) -> List[str]:
        """Gets the languages of this Monster.


        :return: The languages of this Monster.
        :rtype: List[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages: List[str]):
        """Sets the languages of this Monster.


        :param languages: The languages of this Monster.
        :type languages: List[str]
        """

        self._languages = languages

    @property
    def challenge_rating(self) -> int:
        """Gets the challenge_rating of this Monster.


        :return: The challenge_rating of this Monster.
        :rtype: int
        """
        return self._challenge_rating

    @challenge_rating.setter
    def challenge_rating(self, challenge_rating: int):
        """Sets the challenge_rating of this Monster.


        :param challenge_rating: The challenge_rating of this Monster.
        :type challenge_rating: int
        """

        self._challenge_rating = challenge_rating

    @property
    def xp(self) -> int:
        """Gets the xp of this Monster.


        :return: The xp of this Monster.
        :rtype: int
        """
        return self._xp

    @xp.setter
    def xp(self, xp: int):
        """Sets the xp of this Monster.


        :param xp: The xp of this Monster.
        :type xp: int
        """

        self._xp = xp

    @property
    def special_abilities(self) -> List[str]:
        """Gets the special_abilities of this Monster.


        :return: The special_abilities of this Monster.
        :rtype: List[str]
        """
        return self._special_abilities

    @special_abilities.setter
    def special_abilities(self, special_abilities: List[str]):
        """Sets the special_abilities of this Monster.


        :param special_abilities: The special_abilities of this Monster.
        :type special_abilities: List[str]
        """

        self._special_abilities = special_abilities

    @property
    def actions(self) -> List[str]:
        """Gets the actions of this Monster.


        :return: The actions of this Monster.
        :rtype: List[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions: List[str]):
        """Sets the actions of this Monster.


        :param actions: The actions of this Monster.
        :type actions: List[str]
        """

        self._actions = actions

    @property
    def reactions(self) -> List[str]:
        """Gets the reactions of this Monster.


        :return: The reactions of this Monster.
        :rtype: List[str]
        """
        return self._reactions

    @reactions.setter
    def reactions(self, reactions: List[str]):
        """Sets the reactions of this Monster.


        :param reactions: The reactions of this Monster.
        :type reactions: List[str]
        """

        self._reactions = reactions