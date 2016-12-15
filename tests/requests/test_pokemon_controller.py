from test_base import BaseTestCase
from app.models.pokemon import Pokemon
from factories.pokemon_factory import PokemonFactory

class TestPokemonController(BaseTestCase):

    render_templates = False

    def setUp(self):
        PokemonFactory.create_batch(1)

    def tearDown(self):
        Pokemon.query.delete()
        
    def test_pokemon_template_should_be_used(self):
        response = self.client.get("/pokemon/1/")
        self.assert_template_used('pokemon/pokemon.html')