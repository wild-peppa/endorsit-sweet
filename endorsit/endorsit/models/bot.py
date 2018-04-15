from datetime import datetime

from ..plugins.plugins import db, ma


class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    team_id = db.Column(db.Integer, default=0)

    bot_token = db.Column(db.String(256), nullable=False)

    __tablename__ = 'bot'

    def __init__(self,
                 team_id=0,
                 bot_token=''
                 ):
        self.team_id = team_id
        self.bot_token = bot_token


class BotSchema(ma.ModelSchema):
    class Meta:
        model = Bot


bot_schema = BotSchema()

bots_schema = BotSchema(many=True)
