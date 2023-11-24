# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.campaign import Campaign  # noqa: E501
from swagger_server.models.character import Character  # noqa: E501
from swagger_server.models.encounter import Encounter  # noqa: E501
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.monster import Monster  # noqa: E501
from swagger_server.models.npc import NPC  # noqa: E501
from swagger_server.models.spell import Spell  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_campaigns_get(self):
        """Test case for campaigns_get

        Get a list of campaigns
        """
        response = self.client.open(
            '/api/v1/campaigns',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_campaigns_id_delete(self):
        """Test case for campaigns_id_delete

        Delete a campaign by ID
        """
        response = self.client.open(
            '/api/v1/campaigns/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_campaigns_id_get(self):
        """Test case for campaigns_id_get

        Get a campaign by ID
        """
        response = self.client.open(
            '/api/v1/campaigns/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_campaigns_id_put(self):
        """Test case for campaigns_id_put

        Update a campaign by ID
        """
        body = Campaign()
        response = self.client.open(
            '/api/v1/campaigns/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_campaigns_post(self):
        """Test case for campaigns_post

        Create a new campaign
        """
        body = Campaign()
        response = self.client.open(
            '/api/v1/campaigns',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_get(self):
        """Test case for characters_get

        Get a list of characters
        """
        response = self.client.open(
            '/api/v1/characters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_id_delete(self):
        """Test case for characters_id_delete

        Delete a character by ID
        """
        response = self.client.open(
            '/api/v1/characters/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_id_get(self):
        """Test case for characters_id_get

        Get a character by ID
        """
        response = self.client.open(
            '/api/v1/characters/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_id_put(self):
        """Test case for characters_id_put

        Update a character by ID
        """
        body = Character()
        response = self.client.open(
            '/api/v1/characters/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characters_post(self):
        """Test case for characters_post

        Create a new character
        """
        body = Character()
        response = self.client.open(
            '/api/v1/characters',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_get(self):
        """Test case for encounters_get

        Get a list of encounters
        """
        response = self.client.open(
            '/api/v1/encounters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_id_delete(self):
        """Test case for encounters_id_delete

        Delete an encounter by ID
        """
        response = self.client.open(
            '/api/v1/encounters/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_id_get(self):
        """Test case for encounters_id_get

        Get an encounter by ID
        """
        response = self.client.open(
            '/api/v1/encounters/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_id_put(self):
        """Test case for encounters_id_put

        Update an encounter by ID
        """
        body = Encounter()
        response = self.client.open(
            '/api/v1/encounters/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encounters_post(self):
        """Test case for encounters_post

        Create a new encounter
        """
        body = Encounter()
        response = self.client.open(
            '/api/v1/encounters',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_get(self):
        """Test case for items_get

        Get a list of items
        """
        response = self.client.open(
            '/api/v1/items',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_delete(self):
        """Test case for items_id_delete

        Delete an item by ID
        """
        response = self.client.open(
            '/api/v1/items/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_get(self):
        """Test case for items_id_get

        Get an item by ID
        """
        response = self.client.open(
            '/api/v1/items/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_put(self):
        """Test case for items_id_put

        Update an item by ID
        """
        body = Item()
        response = self.client.open(
            '/api/v1/items/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_post(self):
        """Test case for items_post

        Create a new item
        """
        body = Item()
        response = self.client.open(
            '/api/v1/items',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_get(self):
        """Test case for monsters_get

        Get a list of monsters
        """
        response = self.client.open(
            '/api/v1/monsters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_id_delete(self):
        """Test case for monsters_id_delete

        Delete a monster by ID
        """
        response = self.client.open(
            '/api/v1/monsters/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_id_get(self):
        """Test case for monsters_id_get

        Get a monster by ID
        """
        response = self.client.open(
            '/api/v1/monsters/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_id_put(self):
        """Test case for monsters_id_put

        Update a monster by ID
        """
        body = Monster()
        response = self.client.open(
            '/api/v1/monsters/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_monsters_post(self):
        """Test case for monsters_post

        Create a new monster
        """
        body = Monster()
        response = self.client.open(
            '/api/v1/monsters',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_get(self):
        """Test case for npcs_get

        Get a list of NPCs
        """
        response = self.client.open(
            '/api/v1/npcs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_id_delete(self):
        """Test case for npcs_id_delete

        Delete an NPC by ID
        """
        response = self.client.open(
            '/api/v1/npcs/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_id_get(self):
        """Test case for npcs_id_get

        Get an NPC by ID
        """
        response = self.client.open(
            '/api/v1/npcs/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_id_put(self):
        """Test case for npcs_id_put

        Update an NPC by ID
        """
        body = NPC()
        response = self.client.open(
            '/api/v1/npcs/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_npcs_post(self):
        """Test case for npcs_post

        Create a new NPC
        """
        body = NPC()
        response = self.client.open(
            '/api/v1/npcs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_get(self):
        """Test case for spells_get

        Get a list of spells
        """
        response = self.client.open(
            '/api/v1/spells',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_id_delete(self):
        """Test case for spells_id_delete

        Delete a spell by ID
        """
        response = self.client.open(
            '/api/v1/spells/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_id_get(self):
        """Test case for spells_id_get

        Get a spell by ID
        """
        response = self.client.open(
            '/api/v1/spells/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_id_put(self):
        """Test case for spells_id_put

        Update a spell by ID
        """
        body = Spell()
        response = self.client.open(
            '/api/v1/spells/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_spells_post(self):
        """Test case for spells_post

        Create a new spell
        """
        body = Spell()
        response = self.client.open(
            '/api/v1/spells',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Get a list of users
        """
        response = self.client.open(
            '/api/v1/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_delete(self):
        """Test case for users_id_delete

        Delete a user by ID
        """
        response = self.client.open(
            '/api/v1/users/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_get(self):
        """Test case for users_id_get

        Get a user by ID
        """
        response = self.client.open(
            '/api/v1/users/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_put(self):
        """Test case for users_id_put

        Update a user by ID
        """
        body = User()
        response = self.client.open(
            '/api/v1/users/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Create a new user
        """
        body = User()
        response = self.client.open(
            '/api/v1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
