from datetime import datetime

from ..plugins.plugins import db, ma


class Validator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, default=0)

    settings_id = db.Column(db.Integer, default=0)

    input_content = db.Column(db.String(200), default='')

    code = db.Column(db.String(9), default='')

    is_bind = db.Column(db.Boolean, default=False)

    bind_time = db.Column(db.String(20), default='')
    bind_telegram_user_id = db.Column(db.String(20), default='')
    bind_telegram_user_first_name = db.Column(db.String(200), default='')
    bind_telegram_user = db.Column(db.String(100), default='')
    bind_telegram_group_id = db.Column(db.String(20), default='')
    bind_telegram_group = db.Column(db.String(100), default='')

    earned = db.Column(db.Float)

    from_code = db.Column(db.String(9), default='')

    invited_code = db.Column(db.Text, default='')
    invited_count = db.Column(db.Integer, default=0)

    neo_address = db.Column(db.String(100), default='')
    is_exported = db.Column(db.Boolean, default=False)

    create_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    __tablename__ = 'validator'

    def __init__(self,
                 team_id=0,
                 settings_id=0,
                 input_content='',
                 code='',
                 is_bind=False,
                 bind_time='',
                 bind_telegram_user_id='',
                 bind_telegram_user='',
                 bind_telegram_user_first_name='',
                 bind_telegram_group_id='',
                 bind_telegram_group='',
                 earned=0,
                 from_code='',
                 invited_code='',
                 invited_count=0,
                 neo_address='',
                 is_exported=False):
        self.team_id = team_id
        self.settings_id = settings_id
        self.input_content = input_content
        self.code = code
        self.is_bind = is_bind
        self.bind_time = bind_time
        self.bind_telegram_user_id = bind_telegram_user_id
        self.bind_telegram_user = bind_telegram_user
        self.bind_telegram_user_first_name = bind_telegram_user_first_name
        self.bind_telegram_group_id = bind_telegram_group_id
        self.bind_telegram_group = bind_telegram_group
        self.earned = earned
        self.from_code = from_code
        self.invited_code = invited_code
        self.invited_count = invited_count
        self.neo_address = neo_address
        self.is_exported = is_exported


class ValidatorSchema(ma.ModelSchema):
    class Meta:
        model = Validator


validator_schema = ValidatorSchema()

validators_schema = ValidatorSchema(many=True)
