from pprint import pprint

import requests
from base58 import b58decode
from eggit.string import DateTimeUtils
from endorsit.models.bot import Bot
from endorsit.models.settings import Settings
from endorsit.models.validator import Validator
from endorsit.plugins.plugins import db
from endorsit.utils.request import get_data_from_request
from flask import Blueprint, request, json, make_response
from neocore.UInt160 import UInt160

telegram = Blueprint('telegram', __name__)


def validate_neo_addr(address):
    try:
        data = b58decode(address)
        if len(data) != 25:
            return False
        if data[0] != 23:
            return False

        result = UInt160(data[1:21])
        return True
    except:
        return False


@telegram.route("/<string:token>", methods=["POST"])
def airdrop(token):
    def post_telegram(url, chat_id, text, reply_to_message_id):
        r = requests.post(url,
                          headers={
                              'Content-Type': 'application/json'
                          },
                          data=json.dumps({
                              'chat_id': chat_id,
                              'text': text,
                              'reply_to_message_id': reply_to_message_id
                          }).encode('utf-8'))

    data = get_data_from_request(request)
    print('这里是空投', data)
    pprint(data)
    # replay telegram api
    send_to = 'https://api.telegram.org/bot%s/sendMessage' % token

    # text for /code
    text = data['message']['text'] if 'text' in data['message'].keys() else ''

    if not validate_neo_addr(text) and text != '/eds':
        print("validate_neo_addr %s and text is not /eds", text)
        return make_response('true')

    # telegram info from data
    message_id = data['message']['message_id']
    username = '' \
        if 'username' not in data['message']['from'].keys() else \
        data['message']['from']['username']

    first_name = 'my friend' \
        if 'first_name' not in data['message']['from'].keys() else \
        data['message']['from']['first_name']

    user_id = data['message']['from']['id'] if 'id' in data['message']['from'].keys() else ''

    group_id = data['message']['chat']['id'] \
        if 'chat' in data['message'].keys() and 'id' in data['message']['chat'].keys() else \
        ''

    group_title = data['message']['chat']['title'] \
        if 'chat' in data['message'].keys() and 'title' in data['message']['chat'].keys() else \
        ''

    hello_reply = (('@%s' % username) if username else
                   (('Hi, %s' % first_name) if first_name else 'Hi')) + ', '

    def reply(reply_content):
        post_telegram(send_to,
                      group_id,
                      reply_content,
                      message_id)

    check_duplicate_address = Validator.query.filter_by(neo_address=text).first()
    if check_duplicate_address:
        reply('提交失败，该地址已被占用。\nSubmit failed, This address has been used.')
        print('提交失败，该地址已被占用。\nSubmit failed, This address has been used.')

        return make_response('true')

    validator = Validator.query.filter_by(bind_telegram_user_id=user_id).first()

    if text == '/eds':
        print('/eds operation')

        if validator and validator.is_bind and validator.earned:
            reply('邀请 %(invite)s 人\n获得 %(earned)s EDS\n\nInvite %(invite)s\nEarned %(earned)s EDS' % {
                'invite': str(validator.invited_count),
                'earned': str(validator.earned)
            })
        else:
            reply('邀请 0 人\n获得 0 EDS\n\nInvite 0\nEarned 0 EDS')

        return make_response('true')

    if not validator or not validator.is_bind or validator.earned <= 0:
        reply(
            '地址提交成功，但您并未获得EDS。可能原因： \n1、您的账号未绑定 \n2、您未在活动时间内参与 \nThe address is submitted successfully, but you have no EDS. Possible reasons: \n1. Your account is not bound. \n2. You are not involved in the activity time.')
        print('地址提交成功，但您并未获得EDS。可能原因： \n1、您的账号未绑定 \n2、您未在活动时间内参与 \n')
        return make_response('true')

    if validator.neo_address:
        reply(
            '您已提交地址，请勿重复提交。\nYou have submitted the address, please do not repeat the submission.\n\n*******************\n\n邀请 %(invite)s 人\n获得 %(earned)s EDS\n\nInvite %(invite)s\nEarned %(earned)s EDS' % {
                'invite': str(validator.invited_count),
                'earned': str(validator.earned)
            })
        print('您已提交地址，请勿重复提交')
        return make_response('true')

    validator.neo_address = text

    db.session.commit()

    reply(
        '钱包地址提交成功，您获得的EDS将在7个工作日内发放。 \nThe NEO address is submitted successfully, and the EDS you get will be issued within 7 working days.\n\n*******************\n\n邀请 %(invite)s 人\n获得 %(earned)s EDS\n\nInvite %(invite)s\nEarned %(earned)s EDS' % {
            'invite': str(validator.invited_count),
            'earned': str(validator.earned)
        })
    print('钱包地址提交成功，您获得的EDS将在7个工作日内发放。')
    return make_response('true')


@telegram.route('/telegrams/<string:token>', methods=['POST'])
def telegrams(token):
    def post_telegram(url, chat_id, text, reply_to_message_id):
        r = requests.post(url,
                          headers={
                              'Content-Type': 'application/json'
                          },
                          data=json.dumps({
                              'chat_id': chat_id,
                              'text': text,
                              'reply_to_message_id': reply_to_message_id
                          }).encode('utf-8'))

    data = get_data_from_request(request)
    pprint(data)
    # replay telegram api
    send_to = 'https://api.telegram.org/bot%s/sendMessage' % token

    # text for /code
    text = data['message']['text'] if 'text' in data['message'].keys() else ''

    if text == '/eds':
        return make_response('true')

    # telegram info from data
    message_id = data['message']['message_id']
    username = '' \
        if 'username' not in data['message']['from'].keys() else \
        data['message']['from']['username']

    first_name = 'my friend' \
        if 'first_name' not in data['message']['from'].keys() else \
        data['message']['from']['first_name']

    user_id = data['message']['from']['id'] if 'id' in data['message']['from'].keys() else ''

    group_id = data['message']['chat']['id'] \
        if 'chat' in data['message'].keys() and 'id' in data['message']['chat'].keys() else \
        ''

    group_title = data['message']['chat']['title'] \
        if 'chat' in data['message'].keys() and 'title' in data['message']['chat'].keys() else \
        ''

    hello_reply = (('@%s' % username) if username else
                   (('Hi, %s' % first_name) if first_name else 'Hi')) + ', '

    # if text not contains /, return
    if not text or text[0] != '/':
        return make_response('true')

    # get user sent code
    code = text[1:len(text)]

    def reply(reply_content):
        post_telegram(send_to,
                      group_id,
                      reply_content,
                      message_id)

    # get bot info
    bot = Bot.query.filter_by(bot_token=token).first()
    if not bot:
        return make_response('true')

    # get settings by team_id from bot model
    settings = Settings.query.filter_by(team_id=bot.team_id).first()

    # get validator by team_id from bot model and code from user sent
    validator = Validator.query.filter_by(team_id=bot.team_id, code=code).first()

    # if not settings, system error
    if not settings:
        return make_response('true')

    # if not validator, user sent error code
    if not validator:
        reply(hello_reply + settings.error_bind_reply)
        return make_response('true')

    # has the use already submit ?
    validator_old = Validator.query.filter_by(
        team_id=bot.team_id,
        bind_telegram_user_id=user_id).first()

    # if exist record and the code != the old code, repeat operation error
    if validator_old and validator_old.code != code:
        reply(hello_reply + settings.repeat_bind_reply)
        return make_response('true')

    # if validator has already bound
    if validator.is_bind:
        reply(hello_reply + settings.bound_reply)
        return make_response('true')

    # generate record
    validator.is_bind = True
    validator.bind_time = DateTimeUtils.now()
    validator.bind_telegram_user_id = user_id
    validator.bind_telegram_user_first_name = first_name
    validator.bind_telegram_user = username if username else first_name
    validator.bind_telegram_group_id = group_id
    validator.bind_telegram_group = group_title

    if not settings.is_ended:
        validator.earned = settings.init_earn

    from_validator = Validator.query.filter_by(code=validator.from_code).first()
    if from_validator:
        if from_validator.invited_code:
            from_validator.invited_code += ',%s' % validator.code
        else:
            from_validator.invited_code = validator.code

        from_validator.invited_count += 1

        if not settings.is_ended:
            if from_validator.earned < settings.limit_earn:
                if from_validator.earned + settings.invite_earn < settings.limit_earn:
                    from_validator.earned += settings.invite_earn
                else:
                    from_validator.earned = settings.limit_earn

    db.session.commit()

    reply(hello_reply + settings.finish_bind_reply)

    return make_response('true')
