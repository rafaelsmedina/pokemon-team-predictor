import factory
from app import db
from app.models.pokemon import Pokemon

class PokemonFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Pokemon
        sqlalchemy_session = db.session

    num_dex = 15
    species = 'test'
    forme = 'test'
    type1 = 'test'
    type2 = 'test'
    ability1 = 'test'
    ability2 = 'test'
    abilityH = 'test'
    hp = 100
    attack = 100
    defense = 100
    spattack = 100
    spdefense = 100
    speed = 100
    total = 600
    weight = 'test'
    height = 'test'
    dex1 = 'test'
    dex2 = 'test'
    pkmn_class = 'test'
    percent_male = 0.5
    percent_female = 0.5
    pre_evolution = 'test'
    egg_group1 = 'test'
    egg_group2 = 'test'