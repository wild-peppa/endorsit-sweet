from endorsit.exceptions.custom_error import ServiceError
from endorsit.plugins.plugins import db, ma
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from gevent import monkey
from gevent import pywsgi

from config.base import configs
from logger.logger import record_exception, debug_logger
from user.views import user_api

app = Flask(__name__)
monkey.patch_all()


def create_app(config_name):
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)

    # register blueprints area
    app.register_blueprint(user_api, url_prefix='/user')

    # across domain
    CORS(app, supports_credentials=True)

    # plugins register
    db.init_app(app)
    ma.init_app(app)
    return app


# register self-error-handler
@app.errorhandler(ServiceError)
@record_exception
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status = error.status
    return response


# run debug mode
# @run_with_reloader
# def run_debug_mode():
#     debug = create_app('default')
#     debug_server = pywsgi.WSGIServer(('', 5000), DebuggedApplication(debug))
#     debug_logger.info("server debuged...")
#     debug_server.serve_forever()


if __name__ == '__main__':
    # run_debug_mode()

    application = create_app('default')
    server = pywsgi.WSGIServer(('', 5000), application)
    debug_logger.info("server started...")
    server.serve_forever()
