import flask

blueprint = flask.Blueprint('home', 'home')


@blueprint.route('/')
def index():
    return flask.render_template('home/index.html')
