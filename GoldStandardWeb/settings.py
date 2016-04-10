"""
Django settings for GoldStandardWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
  os.path.join(BASE_DIR,'templates'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '59&&jx0d9u8cnm92+*vkh!gesfc@!*n4$+d74vr+^o)a&dp@ln'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'generator',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'constance.backends.database',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'GoldStandardWeb.urls'

WSGI_APPLICATION = 'GoldStandardWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gsdb',
        'USER': 'gsuser',
        'PASSWORD': 'pY8fTPTgAVCTctAP4fg2',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/vhosts/nhla.thecreems.com/static'


#
# This configures the DJANGO_SETTINGS module. To be clear
# this is not a built in capability of DJANGO but rather
# is an add on-module generally available via
# pip or the distribution package manager called django-settings
# 
# https://github.com/jqb/django-settings
# After adding to this list you need to do:
#  ./manage.py settings_initialize
#
#DJANGO_SETTINGS = {
#   'generator_output_directory': ('String', '/tmp'),
#   'generator_http_server_relative_directory':('String', '/tmp'),
#   'generator_JSON_key_file': ('String', '/home/jcreem/nhla/gs_tools/NHLAGS-e8b3911072d5.json'),
#   'generator_gs_tools_path': ('String', '/'),
#}

CONSTANCE_CONFIG = {
   'generator_output_directory': ('/tmp', 'Where to store the PDF files', str),
   'generator_http_server_relative_directory':('/tmp', 'How to find the PDF files relative to the HTTP Server root', str),
   'generator_JSON_key_file': ('/home/nhla/NHLAGS-e8b3911072d5.json','Location of Google sheets json', str),
   'generator_gs_tools_path': ('/', 'Directory containing gs_tools',str),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
#CONSTANCE_REDIS_CONNECTION = {
#    'host': 'localhost',
#    'port': 6379,
#    'db': 0,
#}
#
#CONSTANCE_REDIS_CONNECTION_CLASS = 'redis_cache.get_redis_connection'
