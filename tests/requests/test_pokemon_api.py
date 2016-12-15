from test_base import BaseTestCase
from app.models.pokemon import Pokemon
from factories.pokemon_factory import PokemonFactory

class TestPokemonApi(BaseTestCase):

    def setUp(self):
        PokemonFactory.create_batch(1)

    def tearDown(self):
        Pokemon.query.delete()

    def test_pokemon_api_should_return_json(self):
        response = self.client.get("/api/pokemon/1")
        self.assertEqual(len(response.json), 1)

    def test_pokemon_api_should_return_correct_json(self):
        response = self.client.get("/api/pokemon/1")
        assert 'hp' in response.json['data']
        assert 'attack' in response.json['data']
        assert 'defense' in response.json['data']
        assert 'spattack' in response.json['data']
        assert 'spdefense' in response.json['data']
        assert 'speed' in response.json['data']
        assert 'total' in response.json['data']
        assert 'link' in response.json['data']

    def test_link_in_json_must_be_correct(self):
        response = self.client.get("/api/pokemon/1")
        assert "http://play.pokemonshowdown.com/sprites/bw/bulbasaur.png" in response.json['data']