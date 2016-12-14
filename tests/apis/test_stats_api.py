from test_base import BaseTestCase
from app.models.pokemon import Pokemon
from factories.pokemon_factory import PokemonFactory

class TestPokemonStatsApi(BaseTestCase):

    def setUp(self):
        PokemonFactory.create_batch(1)

    def tearDown(self):
        Pokemon.query.delete()

    def test_stats_api_should_return_json(self):
        response = self.client.get("/api/pokemon/stats/1")
        self.assertEqual(len(response.json), 1)

    def test_stats_api_should_return_correct_json(self):
        response = self.client.get("/api/pokemon/stats/1")
        assert 'hp' in response.json['data']
        assert 'attack' in response.json['data']
        assert 'defense' in response.json['data']
        assert 'spattack' in response.json['data']
        assert 'spdefense' in response.json['data']
        assert 'speed' in response.json['data']
        assert 'total' in response.json['data']