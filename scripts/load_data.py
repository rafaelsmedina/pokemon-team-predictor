import pandas
from flask_script import Command
from app.models.pokemon import Pokemon

class LoadData(Command):

    "Loads pokemon data"

    def run(self):

        data_frame = pandas.read_csv('data/pokemon.csv')
 