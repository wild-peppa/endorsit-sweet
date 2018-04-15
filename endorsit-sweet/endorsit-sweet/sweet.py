from endorsit.config.base import configs
from endorsit.exceptions.custom_error import ServiceError
from endorsit.plugins.plugins import db, ma
from flask import Flask, render_template
from flask import jsonify
from flask_cors import CORS
from gevent import monkey
from gevent import pywsgi
from logger.logger import record_exception, debug_logger
from views.user.views import user_api
from werkzeug.debug import DebuggedApplication
from werkzeug.serving import run_with_reloader

app = Flask(__name__, static_url_path='')
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


# default page
@app.route('/', defaults={'code': None})
@app.route('/from/<string:code>')
def default(code):
    print(code)
    return render_template('index.html')


@app.route('/claim')
def claim():
    return render_template('claim.html')


@app.route('/activity')
def user():
    return render_template('activity.html')


# register self-error-handler
@app.errorhandler(ServiceError)
@record_exception
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    print(error.to_dict())
    return response


# run debug mode
@run_with_reloader
def run_debug_mode():
    debug = create_app('default')
    debug_server = pywsgi.WSGIServer(('0.0.0.0', 8001), DebuggedApplication(debug))
    debug_logger.info("server debuged...")
    debug_server.serve_forever()


if __name__ == '__main__':
    try:
        run_debug_mode()
        # application = create_app('default')
        # server = pywsgi.WSGIServer(('', 8001), application)
        # debug_logger.info("server started...")
        # server.serve_forever()
    except KeyboardInterrupt:
        pass
    except TypeError:
        pass
