class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>'
    JSON_SORT_KEYS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
