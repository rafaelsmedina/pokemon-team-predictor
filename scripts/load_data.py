import pandas
import math
from flask_script import Command
from app.models.pokemon import Pokemon
from app.models.abilities import Ability
from app import db

class LoadData(Command):

    "Loads pokemon data"

    def run(self):

        def handle_nan_str(data):
            return '' if data == 'NaN' else str(data)

        def handle_nan_int(data):
            return 0 if math.isnan(float(data)) else int(data)

        def handle_nan_float(data):
            return 0 if math.isnan(float(data)) else float(data)

        data_frame_pkmn = pandas.read_csv('data/pokemon.csv')

        for index, row in data_frame_pkmn.iterrows():
            pokemon = Pokemon()
            pokemon.num_dex = handle_nan_int(row['ndex'])
            pokemon.species = handle_nan_str(row['species'])
            pokemon.forme = handle_nan_str(row['forme'])
            pokemon.type1 = handle_nan_str(row['type1'])
            pokemon.type2 = handle_nan_str(row['type2'])
            pokemon.ability1 = handle_nan_str(row['ability1'])
            pokemon.ability2 = handle_nan_str(row['ability2'])
            pokemon.abilityH = handle_nan_str(row['abilityH'])
            pokemon.hp = handle_nan_int(row['hp'])
            pokemon.attack = handle_nan_int(row['attack'])
            pokemon.defense = handle_nan_int(row['defense'])
            pokemon.spattack = handle_nan_int(row['spattack'])
            pokemon.spdefense = handle_nan_int(row['spdefense'])
            pokemon.speed = handle_nan_int(row['speed'])
            pokemon.total = handle_nan_int(row['total'])
            pokemon.weight = handle_nan_str(row['weight'])
            pokemon.height = handle_nan_str(row['height'])
            pokemon.dex1 = handle_nan_str(row['dex1'])
            pokemon.dex2 = handle_nan_str(row['dex2'])
            pokemon.pkmn_class = handle_nan_str(row['class'])
            pokemon.percent_male = handle_nan_float(row['percent-male'])
            pokemon.percent_female = handle_nan_float(row['percent-female'])
            pokemon.pre_evolution = handle_nan_str(row['pre-evolution'])
            pokemon.egg_group1 = handle_nan_str(row['egg-group1'])
            pokemon.egg_group2 = handle_nan_str(row['egg-group2'])
            db.session.add(pokemon)

        data_frame_ablt = pandas.read_csv('data/abilities.csv')

        for index, row in data_frame_ablt.iterrows():
            ability = Ability()
            ability.name = row['ability']
            ability.description = row['description']
            db.session.add(ability)

        db.session.commit()
