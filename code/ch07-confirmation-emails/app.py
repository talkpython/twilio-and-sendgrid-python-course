import flask

from db import session
from views import home
from views import admin
from api import order_api
from pathlib import Path

app = flask.Flask(__name__)


def configure():
    configure_routes()
    configure_db()


def configure_routes():
    app.register_blueprint(home.blueprint)
    app.register_blueprint(order_api.blueprint)
    app.register_blueprint(admin.blueprint)


def configure_db():
    db_file = Path(__file__).parent / 'sql' / 'cloud_city.sqlite'
    session.global_init(db_file.as_posix())


if __name__ == '__main__':
    configure()
    app.run(debug=True)
else:
    configure()
