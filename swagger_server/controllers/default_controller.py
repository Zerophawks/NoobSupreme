import connexion
import six

from swagger_server.models.campaign import Campaign  # noqa: E501
from swagger_server.models.character import Character  # noqa: E501
from swagger_server.models.encounter import Encounter  # noqa: E501
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.monster import Monster  # noqa: E501
from swagger_server.models.npc import NPC  # noqa: E501
from swagger_server.models.spell import Spell  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def campaigns_get():  # noqa: E501
    """Get a list of campaigns

     # noqa: E501


    :rtype: List[Campaign]
    """
    return 'do some magic!'


def campaigns_id_delete(id):  # noqa: E501
    """Delete a campaign by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def campaigns_id_get(id):  # noqa: E501
    """Get a campaign by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Campaign
    """
    return 'do some magic!'


def campaigns_id_put(body, id):  # noqa: E501
    """Update a campaign by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Campaign.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def campaigns_post(body):  # noqa: E501
    """Create a new campaign

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Campaign.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def characters_get():  # noqa: E501
    """Get a list of characters

     # noqa: E501


    :rtype: List[Character]
    """
    return 'do some magic!'


def characters_id_delete(id):  # noqa: E501
    """Delete a character by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def characters_id_get(id):  # noqa: E501
    """Get a character by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Character
    """
    return 'do some magic!'


def characters_id_put(body, id):  # noqa: E501
    """Update a character by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def characters_post(body):  # noqa: E501
    """Create a new character

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def encounters_get():  # noqa: E501
    """Get a list of encounters

     # noqa: E501


    :rtype: List[Encounter]
    """
    return 'do some magic!'


def encounters_id_delete(id):  # noqa: E501
    """Delete an encounter by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def encounters_id_get(id):  # noqa: E501
    """Get an encounter by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Encounter
    """
    return 'do some magic!'


def encounters_id_put(body, id):  # noqa: E501
    """Update an encounter by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Encounter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def encounters_post(body):  # noqa: E501
    """Create a new encounter

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Encounter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_get():  # noqa: E501
    """Get a list of items

     # noqa: E501


    :rtype: List[Item]
    """
    return 'do some magic!'


def items_id_delete(id):  # noqa: E501
    """Delete an item by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def items_id_get(id):  # noqa: E501
    """Get an item by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Item
    """
    return 'do some magic!'


def items_id_put(body, id):  # noqa: E501
    """Update an item by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def items_post(body):  # noqa: E501
    """Create a new item

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def monsters_get():  # noqa: E501
    """Get a list of monsters

     # noqa: E501


    :rtype: List[Monster]
    """
    return 'do some magic!'


def monsters_id_delete(id):  # noqa: E501
    """Delete a monster by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def monsters_id_get(id):  # noqa: E501
    """Get a monster by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Monster
    """
    return 'do some magic!'


def monsters_id_put(body, id):  # noqa: E501
    """Update a monster by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Monster.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def monsters_post(body):  # noqa: E501
    """Create a new monster

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Monster.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def npcs_get():  # noqa: E501
    """Get a list of NPCs

     # noqa: E501


    :rtype: List[NPC]
    """
    return 'do some magic!'


def npcs_id_delete(id):  # noqa: E501
    """Delete an NPC by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def npcs_id_get(id):  # noqa: E501
    """Get an NPC by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: NPC
    """
    return 'do some magic!'


def npcs_id_put(body, id):  # noqa: E501
    """Update an NPC by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = NPC.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def npcs_post(body):  # noqa: E501
    """Create a new NPC

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NPC.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def spells_get():  # noqa: E501
    """Get a list of spells

     # noqa: E501


    :rtype: List[Spell]
    """
    return 'do some magic!'


def spells_id_delete(id):  # noqa: E501
    """Delete a spell by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def spells_id_get(id):  # noqa: E501
    """Get a spell by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Spell
    """
    return 'do some magic!'


def spells_id_put(body, id):  # noqa: E501
    """Update a spell by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Spell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def spells_post(body):  # noqa: E501
    """Create a new spell

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Spell.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_get():  # noqa: E501
    """Get a list of users

     # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_id_delete(id):  # noqa: E501
    """Delete a user by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def users_id_get(id):  # noqa: E501
    """Get a user by ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: User
    """
    return 'do some magic!'


def users_id_put(body, id):  # noqa: E501
    """Update a user by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
