from flask import json


def _get_data_from_bytes(data):
    data_str = data.decode('utf-8')
    params = json.loads(data_str)
    return params


def _get_data_from_form(data):
    return data.to_dict()


def _get_origin_data(request):
    return request.data if len(request.data) > 0 else request.form


def get_data_from_request(request):
    data = _get_origin_data(request)
    try:
        if isinstance(data, bytes):
            return _get_data_from_bytes(data)
        else:
            return _get_data_from_form(data)
    except Exception as e:
        return None
