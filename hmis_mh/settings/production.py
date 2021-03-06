from hmis_mh.settings.base import *
import json
with open('/etc/hmis_mh_config.json') as config_file:
        config = json.load(config_file)

DEBUG = True
ALLOWED_HOSTS = ['communitygis.net', 'hmis.communitygis.net', '3.109.54.143']
SECRET_KEY = config['SECRET_KEY'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config['DBNAME'],
        'USER': config['DBUSER'],
        'PASSWORD': config['DBPASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}