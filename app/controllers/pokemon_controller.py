from flask import Blueprint, render_template, json, redirect, url_for
from app.models.pokemon import Pokemon
from app import db

blueprint = Blueprint('pokemon_controller', __name__, url_prefix='/pokemon')

@blueprint.route("/<id>/")
def index(id=id):
    query = db.session.query(Pokemon).filter_by(id=id).first()
    if query != None:
        import pdb; pdb.set_trace()
        pokemon = json.dumps(dict(query))
        return render_template('pokemon/pokemon.html', pokemon=json.loads(pokemon))
    return redirect(url_for('home_controller.index'))


def image_link(forme, id):
    base_string = "http://play.pokemonshowdown.com/sprites/bw/{{substitute-here}}.png"
    if '(' in forme:
        if '(Mega' and 'X)' in forme:
            name = forme.split()[0]
            link = base_string.replace('{{substitute-here}}', name.lower() + '-megax')
        elif '(Mega' and 'Y)' in forme:
            link = base_string.replace('{{substitute-here}}', name.lower() + '-megay')
        elif '(Mega' in forme:
            link = base_string.replace('{{substitute-here}}', name.lower() + '-mega')
        elif 'Pikachu' in forme:
            link = base_string.replace('{{substitute-here}}', name.lower())
        elif '(Alola' in forme:
            link = base_string.replace('{{substitute-here}}', name.lower() + '-alola')
        elif 'Unown' in forme:
            letter = 28 - 870 + int(id)
            letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            if letter >= 2:
                link = base_string.replace('{{substitute-here}}', name.lower() + '-' + letters[letter-2])
            else:
                link = base_string.replace('{{substitute-here}}', name.lower() + '-' + letters[0])
    else:
        link = base_string.replace('{{substitute-here}}', forme.lower())
    return link