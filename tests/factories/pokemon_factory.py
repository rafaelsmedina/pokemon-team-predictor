import factory
from app import db
from app.models.pokemon import Pokemon

class PokemonFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Pokemon
        sqlalchemy_session = db.session

    num_dex = 1
    species = 'Bulbasaur'
    forme = 'Bulbasaur'
    type1 = 'Grass'
    type2 = 'Poison'
    ability1 = 'Overgrow'
    ability2 = 'nan'
    abilityH = 'Chlorophyll'
    hp = 45
    attack = 49
    defense = 49
    spattack = 65
    spdefense = 65
    speed = 45
    total = 318
    weight = '15.2 lbs.'
    height = '2\'04\"'
    dex1 = 'nan'
    dex2 = 'nan'
    pkmn_class = 'Seed Pokemon'
    percent_male = 0.125
    percent_female = 0.875
    pre_evolution = 'nan'
    egg_group1 = 'Monster'
    egg_group2 = 'Grass'