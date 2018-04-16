import os.path as op

from endorsit.config.base import configs
from endorsit.models.bot import Bot
from endorsit.models.settings import Settings
from endorsit.models.validator import Validator
from endorsit.plugins.plugins import admin, db
from flask import Flask
from flask_admin.contrib.fileadmin import FileAdmin

from controllers.custom_view import CustomModelView

app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)
    db.init_app(app)
    admin.init_app(app)
    models = [Settings, Validator, Bot]
    for model in models:
        admin.add_view(
            CustomModelView(model, db.session, category='Models'))

    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name='File Station'))

    return app


if __name__ == '__main__':
    app = create_app('default')
    app.run(debug=True, port=8000)
