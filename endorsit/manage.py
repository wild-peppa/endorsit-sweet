# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
from endorsit.config.base import DefaultConfig
from endorsit.models.bot import Bot
from endorsit.models.settings import Settings
from endorsit.models.users import User
from endorsit.models.validator import Validator
from endorsit.plugins.plugins import db
from flask import Flask
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server

app = Flask(__name__)
# 加载配置集合
app.config.from_object(DefaultConfig)
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Settings=Settings,
                Validator=Validator,
                Bot=Bot)


if __name__ == '__main__':
    manager.run()
