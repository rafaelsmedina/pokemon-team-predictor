from flask import Blueprint, render_template

blueprint = Blueprint('team_controller', __name__, url_prefix='/team')

@blueprint.route("/")
def index():
    return render_template('team/team.html')