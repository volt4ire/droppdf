"""
Django settings for droppdf project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import environ

env = environ.Env()

environ.Env.read_env('.env')

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ii$dm8)3_=9m54n11k_&$82e&)*@9y&hoo2mmth-^!=s0l!&!k'

# SECURITY WARNING: don't run with debug turned on in production!
if env('DJANGO_DEBUG'):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']

#APPEND_SLASH = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'apps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_http_exceptions.middleware.ExceptionHandlerMiddleware',
    'django_http_exceptions.middleware.ThreadLocalRequestMiddleware',
]

ROOT_URLCONF = 'droppdf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'apps/_templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'droppdf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env('DB_NAME'),
        "USER": env('DB_USER'),
        "PASSWORD": env('DB_PASSWORD'),
        "HOST": env('DB_HOST'),
        #"TEST": {
            #'NAME': 'fplan_tests',
        #},
    }
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = (
    (BASE_DIR / 'apps/_static'),
)

MIGRATION_MODULES = {'apps': 'apps._migrations'}

# AWS Settings
AWS_ACCESS_KEY = env('AWS_ACCESS_KEY')
AWS_SECRET_KEY = env('AWS_SECRET_KEY')
AWS_S3_CUSTOM_DOMAIN = env('AWS_CUSTOM_DOMAIN')

AWS_ANNOTATIONS_BUCKET = env('AWS_ANNOTATIONS_BUCKET')
AWS_OCR_BUCKET = env('AWS_OCR_BUCKET')
AWS_FINGERPRINTER_BUCKET = env('AWS_FINGERPRINTER_BUCKET')


# max number simultaneous ocr process 
MAX_SIM_OCR_PROCESSES = env('MAX_SIM_OCR_PROCESSES')

#celery
CELERY_RESULT_BACKEND = 'django-db'
BROKER_URL = env('BROKER_URL')
