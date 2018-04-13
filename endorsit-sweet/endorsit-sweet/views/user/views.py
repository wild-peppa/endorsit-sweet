import random

from endorsit.exceptions.custom_error import ServiceError
from endorsit.models.settings import Settings, setting_schema
from endorsit.models.users import User, users_schema, user_schema
from endorsit.models.validator import Validator
from endorsit.plugins.plugins import db
from endorsit.response.utils import success_response
from endorsit.utils.request import get_data_from_request
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
    if user:
        output = user_schema.dump(user).data
        return success_response(output)
    raise ServiceError(200000)


@user_api.route("/queryUsers", methods=["GET"])
def query_users():
    users = User.query.all()
    if users:
        output = users_schema.dump(users).data
        return success_response(output)
    raise ServiceError(200000)


@user_api.route("/update", methods=["GET"])
def update():
    user = db.session.query(User).filter_by(name='update').first()
    if user:
        user.name = 'update2'
        db.session.commit()
        return success_response('Update success')
    raise ServiceError(200000)


# return settings
@user_api.route("/settings", methods=["GET"])
def settings():
    setting_result = db.session.query(Settings).first()
    if setting_result:
        # todo accroding to airdrop time to change digst's value
        del setting_result.ended_digest
        output = setting_schema.dump(setting_result).data
        return success_response(output)
    raise ServiceError(200000)


# validate mail code exist?code:newcode
@user_api.route("/code", methods=["POST"])
def code():
    data = get_data_from_request(request)
    print(data)
    if 'input_content' not in data.keys() or not data['input_content']:
        raise ServiceError(100001)
    old_validator = Validator.query.filter_by(input_content=data['input_content']).first()
    if old_validator:
        return success_response(old_validator.code)

    new_code = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', 8))
    try:
        validator = Validator(
            team_id=int(data['team_id']),
            settings_id=int(data['settings_id']),
            input_content=data['input_content'],
            code=new_code
        )
    except Exception:
        raise ServiceError(100001)

    '''
    query with condition(team_id, from_code), (exist and !bind)?do:notdo
    '''
    if 'from_code' in data.keys():
        from_validator = Validator.query.filter_by(team_id=int(data['team_id']),
                                                   code=data['from_code']).first()
        if from_validator and from_validator.is_bind == False:
            validator.from_code = data['from_code']
            validator.is_bind = True
    db.session.add(validator)
    db.session.commit()
    return success_response(new_code)


@user_api.route("/earn", methods=["GET"])
def earn():
    code_arg = request.args.get('code')
    validator = Validator.query.filter_by(code=code_arg).first()
    if not validator:
        raise ServiceError(200003)

    data = {}
    data['earned'] = validator.earned
    data['invited'] = validator.invited_count

    return success_response(data)
