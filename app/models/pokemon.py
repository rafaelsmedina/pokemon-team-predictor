from sqlalchemy import Column, Integer, String, Float
from app import db

class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    num_dex = Column(Integer)
    species = Column(String)
    forme = Column(String)
    type1 = Column(String)
    type2 = Column(String)
    ability1 = Column(String)
    ability2 = Column(String)
    abilityH = Column(String)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    spattack = Column(Integer)
    spdefense = Column(Integer)
    speed = Column(Integer)
    total = Column(Integer)
    weight = Column(String)
    height = Column(String)
    dex1 = Column(String)
    dex2 = Column(String)
    pkmn_class = Column(String)
    percent_male = Column(Float)
    percent_female = Column(Float)
    pre_evolution = Column(String)
    egg_group1 = Column(String)
    egg_group2 = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'num_dex', self.num_dex
        yield 'species', self.species
        yield 'forme', self.forme
        yield 'type1', self.type1
        yield 'type2', self.type2
        yield 'ability1', self.ability1
        yield 'ability2', self.ability2
        yield 'abilityH', self.abilityH
        yield 'hp', self.hp
        yield 'attack', self.attack
        yield 'defense', self.defense
        yield 'spattack', self.spattack
        yield 'spdefense', self.spdefense
        yield 'speed', self.speed
        yield 'total', self.total
        yield 'weight', self.weight
        yield 'height', self.height
        yield 'dex1', self.dex1
        yield 'dex2', self.dex2
        yield 'pkmn_class', self.pkmn_class
        yield 'percent_male', self.percent_male
        yield 'percent_female', self.percent_female
        yield 'pre_evolution', self.pre_evolution
        yield 'egg_group1', self.egg_group1
        yield 'egg_group2', self.egg_group2