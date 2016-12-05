from app import flask, db
from flask.ext.testing import TestCase


class BaseTestCase(TestCase):


    def create_app(self):
        flask.config.from_object('config.Testing')
        db.create_all()
        return flask



