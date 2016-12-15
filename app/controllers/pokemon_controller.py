from flask import Blueprint, render_template, json, redirect, url_for
from app.models.pokemon import Pokemon
from app import db

blueprint = Blueprint('pokemon_controller', __name__, url_prefix='/pokemon')

@blueprint.route("/<id>/")
def index(id=id):
    if int(id) <= db.session.query(Pokemon).count():
        return render_template('pokemon/pokemon.html', id=id)
    return redirect(url_for('home_controller.index'))
