from endorsit.exceptions.custom_error import ServiceError
from endorsit.models.users import User, users_schema, user_schema
from endorsit.plugins.plugins import db
from endorsit.response.utils import success_response
# from user import user_api
from flask import Blueprint, request
from sqlalchemy.exc import ProgrammingError, IntegrityError

user_api = Blueprint('user', __name__)

'''
Example for flask-sqlachemy CRUD
'''


@user_api.route("/insert", methods=["POST"])
def insert_user():
    print(request.get_data())
    name = request.form.get('name', 'admin')
    age = request.form.get('age', 0)
    try:
        # name = '%s%s' % ('zz', str(time.time()))
        user_model = User(name, age)
        db.session.add(user_model)
        db.session.commit()
    except ProgrammingError:
        raise ServiceError(200001)
    except IntegrityError:
        raise ServiceError(200002)
    return success_response('insert success')


@user_api.route("/queryUser", methods=["GET"])
def query_user():
    name = request.args.get('name')
    user = User.query.filter_by(name=name).first()
    output = user_schema.dump(user).data
    return success_response(output)


@user_api.route("/queryUsers", methods=["GET"])
def query_users():
    users = User.query.all()
    output = users_schema.dump(users).data
    return success_response(output)


@user_api.route("/update", methods=["GET"])
def update():
    user = db.session.query(User).filter_by(name='update').first()
    if user:
        user.name = 'update2'
        db.session.commit()
        return success_response('Update success')
    return success_response('No data')
