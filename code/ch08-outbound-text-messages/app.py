import json

import flask
from pathlib import Path

from db import session
from infrastructure import app_secrets
from views import home
from views import admin
from api import order_api
from pathlib import Path

app = flask.Flask(__name__)


def configure():
    configure_secrets()
    configure_routes()
    configure_db()


def configure_secrets():
    file = Path(__file__).parent / "secrets.json"
    if not file.exists():
        raise Exception("Cannot start, secrets.json file is missing. Need to copy the template over?")

    with open(file, 'r') as fin:
        secrets = json.load(fin)

        sendgrid_ = secrets['sendgrid']
        app_secrets.sendgrid_api_key = sendgrid_['secret_key']
        app_secrets.sendgrid_key_name = sendgrid_['key_name']

        twilio_keys = secrets['twilio']
        app_secrets.twilio_sid = twilio_keys['sid']
        app_secrets.twilio_key = twilio_keys['auth_token']


def configure_routes():
    app.register_blueprint(home.blueprint)
    app.register_blueprint(order_api.blueprint)
    app.register_blueprint(admin.blueprint)


def configure_db():
    db_file = Path(__file__).parent / 'sql' / 'cloud_city.sqlite'
    session.global_init(db_file.as_posix())


if __name__ == '__main__':
    configure()
    app.run(host='127.0.0.1', port=8000, debug=True)
else:
    configure()
