class Config(object):
    DEBUG = False
    TESTING = False

class Development(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///pokemonTeamBuilderTest'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Testing(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
