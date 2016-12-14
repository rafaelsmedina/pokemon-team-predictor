from flask import Blueprint, jsonify
from app.models.pokemon import Pokemon
from app import db


blueprint = Blueprint('pokemon_api', __name__, url_prefix='/api/pokemon')

@blueprint.route("/")
def list():
    pokemons = db.session.query(Pokemon).all()
    return jsonify(data=[dict(n) for n in pokemons])

@blueprint.route("/stats/<id>")
def stats(id=id):
    pokemon = db.session.query(Pokemon).filter_by(id=id).first()
    if pokemon != None:
        return jsonify(data=dict(pokemon))
    return None