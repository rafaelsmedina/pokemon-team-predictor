import factory
from app import db
from app.models.abilities import Ability

class AbilityFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Ability
        sqlalchemy_session = db.session

    name = 'Lorem Ipsum'
    description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'