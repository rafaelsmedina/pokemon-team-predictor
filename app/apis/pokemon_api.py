from flask import Blueprint, jsonify, json
from app.models.pokemon import Pokemon
from app import db


blueprint = Blueprint('pokemon_api', __name__, url_prefix='/api/pokemon')

@blueprint.route("/")
def list():
    pokemons = db.session.query(Pokemon).all()
    return jsonify(data=[dict(n) for n in pokemons])

@blueprint.route("/<id>")
def stats(id=id):
    pokemon = db.session.query(Pokemon).filter_by(id=id).first()
    if pokemon != None:
        link = image_link(pokemon.forme, pokemon.id)
        type1_img = type_image(pokemon.type1)
        type2_img = type_image(pokemon.type2)
        pokemon = json.dumps(dict(pokemon))
        pokemon = pokemon.replace("}", ", \"img-link\": \"" + link + "\", \"type1-image\": \"" + type1_img + "\", \"type2-image\": \"" + type2_img + "\"}")
        return jsonify(data=pokemon)
    return None

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
    else:
        link = base_string.replace('{{substitute-here}}', forme.lower())
    return link

def type_image(type):
    return "http://play.pokemonshowdown.com/sprites/types/" + type + ".png"