from test_base import BaseTestCase


class TestHomeController(BaseTestCase):

    def test_team_path_should_be_ok(self):
        response = self.client.get("/team/")
        self.assert_200(response)
