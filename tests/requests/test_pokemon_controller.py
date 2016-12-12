from test_base import BaseTestCase


class TestPokemonController(BaseTestCase):

    def test_pokemon_path_should_be_ok(self):
        response = self.client.get("/pokemon/10/")
        self.assert_200(response)
