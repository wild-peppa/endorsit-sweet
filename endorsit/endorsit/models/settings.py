from datetime import datetime

from ..plugins.plugins import db, ma


class Settings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)

    logo = db.Column(db.String(100), default='')
    logo_link = db.Column(db.String(200), default='')

    contact_alt = db.Column(db.String(100), default='')
    contact_link = db.Column(db.String(100), default='')

    digest = db.Column(db.String(500), default='')
    ended_digest = db.Column(db.String(500), default='')

    input_type_id = db.Column(db.Integer, default=0)
    input_content_tip = db.Column(db.String(100), default=0)

    step1_desc = db.Column(db.String(200), default='')
    step2_desc = db.Column(db.String(200), default='')

    ended_step1_desc = db.Column(db.String(200), default='')
    ended_step2_desc = db.Column(db.String(200), default='')

    share_link_domain = db.Column(db.String(100), default='')

    result1_desc = db.Column(db.String(200), default='')
    result2_desc = db.Column(db.String(200), default='')

    team_id = db.Column(db.Integer, default=0)

    init_earn = db.Column(db.Integer, default=0)
    invite_earn = db.Column(db.Integer, default=0)
    limit_earn = db.Column(db.Integer, default=0)

    bound_reply = db.Column(db.String(500), default='')
    finish_bind_reply = db.Column(db.String(500), default='')
    error_bind_reply = db.Column(db.String(500), default='')
    repeat_bind_reply = db.Column(db.String(500), default='')

    extract_token_tip = db.Column(db.String(500), default='')

    is_ended = db.Column(db.Boolean, default=False)

    create_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self,
                 logo='',
                 logo_link='',
                 contact_alt='',
                 contact_link='',
                 digest='',
                 ended_digest='',
                 input_type_id=0,
                 input_content_tip='',
                 step1_desc='',
                 step2_desc='',
                 ended_step1_desc='',
                 ended_step2_desc='',
                 share_link_domain='',
                 result1_desc='',
                 result2_desc='',
                 team_id=0,
                 init_earn=0,
                 invite_earn=0,
                 limit_earn=0,
                 bound_reply='',
                 finish_bind_reply='',
                 error_bind_reply='',
                 repeat_bind_reply='',
                 extract_token_tip='',
                 is_ended=False):
        self.logo = logo
        self.logo_link = logo_link
        self.contact_alt = contact_alt
        self.contact_link = contact_link
        self.digest = digest
        self.ended_digest = ended_digest
        self.input_type_id = input_type_id
        self.input_content_tip = input_content_tip
        self.step1_desc = step1_desc
        self.step2_desc = step2_desc
        self.ended_step1_desc = ended_step1_desc
        self.ended_step2_desc = ended_step2_desc
        self.share_link_domain = share_link_domain
        self.result1_desc = result1_desc
        self.result2_desc = result2_desc
        self.team_id = team_id
        self.init_earn = init_earn
        self.invite_earn = invite_earn
        self.limit_earn = limit_earn
        self.bound_reply = bound_reply
        self.finish_bind_reply = finish_bind_reply
        self.error_bind_reply = error_bind_reply
        self.repeat_bind_reply = repeat_bind_reply
        self.extract_token_tip = extract_token_tip
        self.is_ended = is_ended


class SettingsSchema(ma.ModelSchema):
    class Meta:
        model = Settings


setting_schema = SettingsSchema()

settings_schema = SettingsSchema(many=True)
