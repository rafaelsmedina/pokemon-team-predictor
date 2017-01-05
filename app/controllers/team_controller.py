from flask import Blueprint, render_template, json, redirect, url_for
from app.models.pokemon import Pokemon
from app import db

blueprint = Blueprint('team_controller', __name__, url_prefix='/team')

@blueprint.route("/<pkmn1>/")
@blueprint.route("/<pkmn1>/<pkmn2>/")
@blueprint.route("/<pkmn1>/<pkmn2>/<pkmn3>/")
@blueprint.route("/<pkmn1>/<pkmn2>/<pkmn3>/<pkmn4>/")
@blueprint.route("/<pkmn1>/<pkmn2>/<pkmn3>/<pkmn4>/<pkmn5>/")
@blueprint.route("/<pkmn1>/<pkmn2>/<pkmn3>/<pkmn4>/<pkmn5>/<pkmn6>/")
def index(pkmn1, pkmn2=None, pkmn3=None, pkmn4=None, pkmn5=None, pkmn6=None):
    id_list = [pkmn1, pkmn2, pkmn3, pkmn4, pkmn5, pkmn6]
    id_list = filter(None, id_list)
    id_list = filter(is_id_valid, id_list)
    print id_list
    if len(id_list) > 0:
        return render_template('team/team.html', id_list=id_list)
    return redirect(url_for('home_controller.index'))


def is_id_valid(id):
    if (int(id) > 0) and (int(id) <= db.session.query(Pokemon).count()):
        return True
    return False