class Config:
    @staticmethod
    def init_app(app):
        pass


class DefaultConfig(Config):
    SECRET_KEY = 'secret key xxx'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@ip:port/database?charset=utf8mb4'
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_PRE_PING = True
    SQLALCHEMY_POOL_RECYCLE = 499
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = False


configs = {
    'default': DefaultConfig
}
