import os

class Config:

    NEWS_API_BASE_URL =  'https://newsapi.org/v2/sources?apiKey=8042f30000994df78898ee8fafe63983'
    NEWS_API_ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
