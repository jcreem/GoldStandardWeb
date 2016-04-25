"""
Django settings for GoldStandardWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

#
# We've made a choice here. Not a great choice for a large scalable website
# but probably file for here. The Settings file often needs to contain
# 'sensative' values like database passwords or the django secret key.
# Generally these ar placed directly in settings which is fine until someone
# commits the file to a semi-public repository someplace or even just has
# a copy sitting around on their local machine that gets compromised. So
# we store senative values in a config file intended to be unique to the
# server or development setup being used to reduce that risk. It does meaning
# more overhead when settings is invoked.
#
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('/etc/django_keys/django.cfg')






# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY=config.get("Generator","SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
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
        'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
        'NAME'     : config.get("Generator","DATABASE_NAME"),
        'USER'     : config.get("Generator","DATABASE_USER"),
        'PASSWORD' : config.get('Generator',"DATABASE_PASSWORD"),
        'HOST'      : config.get('Generator',"DATABASE_HOST"),
        'PORT'     : '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#
# We use the Constance package in order to define overall configuration
# parameters that control the operation of the Gold Standard generator
# application. In most cases, the defaults we use here are not 'good'
# intial defaults - meaning, when one does an intial installation, you'll
# need to visit the admin page for the application and pick values that
# make sense for the install.
#
CONSTANCE_CONFIG = {
   #
   # generator_output_directory should be a location in the filesystem that
   # is visible to the web server that is serving the application
   #
   'generator_output_directory': ('/', 'Where to store the PDF files', str),
   #
   # generator_http_server_relative_directory is the web server relative path
   # to generator_output_directory. Typically would match some number of
   # of the suffix directories from generator_output_directory
   #
   'generator_http_server_relative_directory':('/', \
     'How to find the PDF files relative to the HTTP Server root', str),
   #
   # generator_JSON_key_file is a JSON file that will support Authentication
   # within the google docs sheets that we use to collaborate on when we
   # are gathering inputs for the Gold Standard
   #
   'generator_JSON_key_file': ('/home/nhla/NHLAGS-e8b3911072d5.json',\
     'Location of Google sheets json', str),

   #
   # The django generator application is largely a 'front end' to a python
   # package we call gs_tools (Gold Standard Tools) that supports things like
   # converting a google docs sheet into a well-formatted Gold Standard
   # PDF. This should be the path to the directory that contains gs_tools
   #
   'generator_gs_tools_path': ('/', \
     'Directory containing gs_tools directory/package', str),
   #
   # When we are done with the Gold Standard, we generally get it printed to
   # distribute it. This is handled be emailing it to a printing company
   # and telling them how many copes to make. generator_Senate_GS_Print_Copies
   # indicates the # of copies we want if the Gold Standard is for the Senate
   #
   'generator_Senate_GS_Print_Copies': (60, \
     'Number of copies to get printed for Senate GS', int),
   #
   # Same as generator_Senate_GS_Print_Copies but for the House
   #
   'generator_House_GS_Print_Copies': (300, \
      'Number of copies to get printed for House GS', int),
   #
   # When we generate the email to the production company, this is the Time
   # that we request that the standard be ready for pick up
   #
   'generator_Printer_Pickup_Time':('7:30AM',\
     'Time that we want printer to have GS ready', str),

   #
   # generator_Requestor_Name is intended to be a human name to drop at the
   # bottom of the email that we send to the printer when we request they
   # print the standard.
   #
   'generator_Requestor_Name' : ('Jefferson',\
     "Name to use to close out GS related emails.", str),
   #
   # generator_png_dpi controls the output resolution for the PNG files that
   # we generate from the PDF. This gets used for things like email
   # versions of the Gold Standard. Needs to be high enough resolution so
   # the document is readable but not so high that it fills up people's
   # inboxes
   #
   'generator_png_dpi':(90,\
     "Dots per inch of generated PNG files for the Gold Standard", int),

   #
   # generator_gs_production_email_to is the email address that send the
   # request to print the gold standard to and _cc is who we CC when we
   # sent that email.
   #
   'generator_gs_production_email_to':('test@test.com', "List of comma " +\
      "separated addresses to email to have Gold Standard printed", str),
   'generator_gs_production_email_cc':('test1@test.com, test2@test.com', \
     "List of comma separated addresses to CC when Gold Standard printed", str),

   #
   # generator_gs_collab_email_to is the email address to which we send the
   # intiail email requesting people help on contribting input to the GS
   #
   'generator_gs_collab_email_to':('test@test.com', \
     "List of comma separated addresses to send Collaboration email to", str),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

#
# CONSTANCE performance can apparently be improved with a caching backends
# like REDIS. Not currently configuring that
#
#CONSTANCE_REDIS_CONNECTION = {
#    'host': 'localhost',
#    'port': 6379,
#    'db': 0,
#}
#
#CONSTANCE_REDIS_CONNECTION_CLASS = 'redis_cache.get_redis_connection'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL=config.get("Generator","STATIC_URL")
STATIC_ROOT=config.get("Generator","STATIC_ROOT")
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MY_TEMPLATE_DIRS = os.path.join(BASE_DIR,'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [MY_TEMPLATE_DIRS,
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
