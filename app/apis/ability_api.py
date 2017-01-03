from flask import Blueprint, jsonify, json
from app.models.abilities import Ability
from app import db

blueprint = Blueprint('ability_api', __name__, url_prefix='/api/ability')

@blueprint.route("/")
def list():
    abilities = db.session.query(Ability).all()
    return jsonify(data=[dict(n) for n in abilities])

@blueprint.route("/<id>")
def stats(id=id):
    ability = db.session.query(Ability).filter_by(id=id).first()
    if ability != None:
        ability = json.dumps(dict(ability))
        return jsonify(data=ability)
    return None