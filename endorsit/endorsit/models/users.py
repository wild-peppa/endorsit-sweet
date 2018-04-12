from ..plugins.plugins import db, ma

#example
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    age = db.Column(db.Integer)
    tel = db.Column(db.String(16))

    def __init__(self, name, age):
        self.name = name,
        self.age = age

    def __repr__(self):
        return '<User {}>'.format(self.name)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


user_schema = UserSchema()

users_schema = UserSchema(many=True)
