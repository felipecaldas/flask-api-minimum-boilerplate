import os


class Config:
    ENV = os.environ.get('ENV')

    @staticmethod
    def init_app(app):
        pass


class LocalConfig(Config):
    DEBUG = True


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {
    'local': LocalConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
