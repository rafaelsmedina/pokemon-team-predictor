from flask import Blueprint, render_template, json
from app.models.pokemon import Pokemon
from app import db

blueprint = Blueprint('pokemon_controller', __name__, url_prefix='/pokemon')

@blueprint.route("/<id>")
def index(id=id):
    pokemon = json.dumps(dict(db.session.query(Pokemon).filter_by(id=id).first()))
    return render_template('pokemon/pokemon.html', pokemon=json.loads(pokemon))