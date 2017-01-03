from test_base import BaseTestCase
from app.models.abilities import Ability
from factories.ability_factory import AbilityFactory

class TestAbilityApi(BaseTestCase):

    def setUp(self):
        AbilityFactory.create_batch(10)

    def tearDown(self):
        Ability.query.delete()

    def test_api_should_return_10_pokemon(self):
        response = self.client.get("/api/ability/")
        self.assertEqual(len(response.json['data']), 10)