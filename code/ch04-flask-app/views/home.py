import flask

blueprint = flask.Blueprint('home', 'home')


@blueprint.route('/')
def index():
    return "Hello world!"
