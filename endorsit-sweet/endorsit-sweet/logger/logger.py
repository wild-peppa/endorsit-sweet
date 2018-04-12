import logging.config
import os


def get_logger(logger_name):
    config_path = os.path.join(os.path.dirname(__file__), 'logger.config')
    logging.config.fileConfig(config_path)
    logger = logging.getLogger(logger_name)
    return logger


debug_logger = get_logger('debug')
error_logger = get_logger('error')


def record_exception(func):
    def wrapper(e):
        error_logger.exception(e)
        return func(e)

    return wrapper


def record_debug(func):
    def wrapper(e):
        debug_logger.info(e)
        return func(e)

    return wrapper
