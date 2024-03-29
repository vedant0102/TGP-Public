"""
Django settings for thegreyplanet project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import json
import os

dir_name = os.path.dirname( __file__ )
path = os.path.join( dir_name, '../../config.json' )
f = open( path )
private_data = json.load( f )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r$ecu)l_6q9d@%75@*x%xfizg@5xge7#4mvi(o%&5cd=e4vzn='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1','139.59.34.95','thegreyplanet.com','www.thegreyplanet.com']

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django_summernote',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.sites',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thegreyplanet.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS' : [],
        'APP_DIRS' : True,
        'OPTIONS' : {
            'context_processors' : [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'thegreyplanet.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
    }
else:
    DATABASES = {
        'default' : {
            'ENGINE' : 'django.db.backends.postgresql_psycopg2',
            'NAME' : 'planetdb',
            'USER' : 'dbadmin',
            'PASSWORD' : 'qwerty123',
            'HOST' : 'localhost',
            'PORT' : '',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME' : 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
STATIC_ROOT = os.path.join( BASE_DIR, 'static' )
MEDIA_URL = '/media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_THEME = 'bs4'

SITE_ID = 1

NEWSLETTER_RICHTEXT_WIDGET = "django_summernote.widgets.SummernoteWidget"

# DataFlair
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = private_data['newsletter_email']
EMAIL_HOST_PASSWORD = private_data['newsletter_email_passwd']

SUMMERNOTE_CONFIG = {
    'summernote' : {

        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline','italic','strikethrough','superscript','subscript','clear']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['insert', ['link', 'picture', 'video','hr']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

},

}
