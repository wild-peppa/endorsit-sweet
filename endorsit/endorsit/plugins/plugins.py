from flask_admin import Admin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
admin = Admin(name=u'后台管理系统')
