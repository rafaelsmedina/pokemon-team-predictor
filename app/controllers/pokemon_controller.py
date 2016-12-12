from flask import Blueprint, render_template, json, redirect
from app.models.pokemon import Pokemon
from app import db

blueprint = Blueprint('pokemon_controller', __name__, url_prefix='/pokemon')

@blueprint.route("/<id>/")
def index(id=id):
    query = db.session.query(Pokemon).filter_by(id=id).first()
    if query != None:
        pokemon = json.dumps(dict(query))
        return render_template('pokemon/pokemon.html', pokemon=json.loads(pokemon))
    return render_template('home/index.html')