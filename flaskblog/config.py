import os

from sqlalchemy.util import non_memoized_property
#import json
#
#with open('/etc/config-flask_blog.json') as config_file:
#    config = json.load(config_file)

class Config:
    SECRET_KEY = "457e9068bdca2a4d6cdf300d3e510c49" #reandoemly genrtated temp key
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = None#config.get('EMAIL_USER')
    MAIL_PASSWORD = None#config.get('EMAIL_PASS')
