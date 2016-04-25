"""
Django settings for GoldStandardWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/django_keys/generator_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True

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



CONSTANCE_CONFIG = {
   'generator_output_directory': ('/', 'Where to store the PDF files', str),
   'generator_http_server_relative_directory':('/', 'How to find the PDF files relative to the HTTP Server root', str),
   'generator_JSON_key_file': ('/home/nhla/NHLAGS-e8b3911072d5.json','Location of Google sheets json', str),
   'generator_gs_tools_path': ('/', 'Directory containing gs_tools directory/package',str),
   'generator_Senate_GS_Print_Copies': (60, 'Number of copies to get printed for Senate GS',int),
   'generator_House_GS_Print_Copies': (300, 'Number of copies to get printed for House GS',int),
   'generator_Printer_Pickup_Time':('7:30AM','Time that we want printer to have GS ready',str),
   'generator_Requestor_Name' : ('Jeff',"Name to use to close out GS related emails.",str),
   'generator_png_dpi':(90,"Dots per inch of generated PNG files for the Gold Standard",int),
   'generator_gs_production_email_to':('test@test.com', \
     "List of comma separated addresses to email to have Gold Standard printed", str),
   'generator_gs_production_email_cc':('test1@test.com, test2@test.com', \
     "List of comma separated addresses to CC email when Gold Standard printed", str),
   'generator_gs_collab_email_to':('test@test.com', \
     "List of comma separated addresses to send Gold Standard Collaboration email to", str),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
#CONSTANCE_REDIS_CONNECTION = {
#    'host': 'localhost',
#    'port': 6379,
#    'db': 0,
#}
#
#CONSTANCE_REDIS_CONNECTION_CLASS = 'redis_cache.get_redis_connection'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/html/static'

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
