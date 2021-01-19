import flask
from views import home
from api import order_api

app = flask.Flask(__name__)

app.register_blueprint(home.blueprint)
app.register_blueprint(order_api.blueprint)

if __name__ == '__main__':
    app.run()
