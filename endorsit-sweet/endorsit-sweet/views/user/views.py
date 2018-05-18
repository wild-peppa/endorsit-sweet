import datetime
import random

from endorsit.exceptions.custom_error import ServiceError
from endorsit.models.settings import Settings, setting_schema
from endorsit.models.validator import Validator
from endorsit.plugins.plugins import db
from endorsit.response.utils import success_response
from endorsit.utils.request import get_data_from_request
# from user import user_api
from flask import Blueprint, request

user_api = Blueprint('user', __name__)


# return settings
@user_api.route("/settings", methods=["GET"])
def settings():
    setting_result = db.session.query(Settings).first()
    if setting_result:
        # todo accroding to airdrop time to change digst's value
        output = setting_schema.dump(setting_result).data
        return success_response(output)
    raise ServiceError(200000)


# validate mail code exist?code:newcode
@user_api.route("/code", methods=["POST"])
def code():
    data = get_data_from_request(request)
    print(data)
    if 'input_content' not in data.keys() \
            or not data['input_content'] \
            or 'team_id' not in data.keys() \
            or not data['team_id'] \
            or 'settings_id' not in data.keys() \
            or not data['settings_id']:
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
            code=new_code,
            create_at=datetime.datetime.now(),
            update_at=datetime.datetime.now()
        )
    except Exception:
        raise ServiceError(100001)

    '''
    query with condition(team_id, from_code), (exist and !bind)?do:notdo
    '''
    if 'from_code' in data.keys():
        from_validator = Validator.query.filter_by(team_id=int(data['team_id']),
                                                   code=data['from_code']).first()
        if from_validator and from_validator.is_bind:
            validator.from_code = data['from_code']
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
