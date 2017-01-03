from test_base import BaseTestCase
from app.models.abilities import Ability
from factories.ability_factory import AbilityFactory

class TestAbilityApi(BaseTestCase):

    def setUp(self):
        AbilityFactory.create_batch(1)

    def tearDown(self):
        Ability.query.delete()

    def test_ability_api_should_return_json(self):
        response = self.client.get("/api/ability/1")
        self.assertEqual(len(response.json), 1)

    def test_ability_api_should_return_correct_json(self):
        response = self.client.get("/api/ability/1")
        assert 'name' in response.json['data']
        assert 'description' in response.json['data']

