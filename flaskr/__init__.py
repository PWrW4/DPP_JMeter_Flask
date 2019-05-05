import os

from flask import Flask


def create_app(config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py', silent=False)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import api

    # a simple page that says hello
    @app.route('/')
    def index():
        return 'Hello To Bank Czasu sp. z o.o.'

    app.register_blueprint(api.bp, url_prefix='/api')

    return app
