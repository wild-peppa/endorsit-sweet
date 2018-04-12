from flask import jsonify

from ..exceptions.code import Code


def success_response(data=None):
    return jsonify({"status": 'success', "data": data})


def error_response(code, err=None):
    if err is not None:
        return jsonify({"status": 'error', 'error_code': code, "error_msg": err})
    return jsonify({"status": 'error', 'error_code': code, "error_msg": Code.msg[code]})
