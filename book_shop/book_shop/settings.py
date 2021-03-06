"""
Django settings for book_shop project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xvq0ev%(zyic4!&shr-ur-p^*e1kq$b&lu7v(sr!#c_v&vq#y7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'cart',
    'orders',
    'paypal.standard.ipn',
    'payment',
    # 'ckeditor',
    # 'ckeditor_uploader',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'book_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',  #module_name.context_processors.function_name
            ],
        },
    },
]

WSGI_APPLICATION = 'book_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('uk', 'Українська'),
    ('en', 'English'),
#    ('pl', 'Polski'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

    # '/var/www/static/',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

CART_SESSION_ID = 'cartss'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
PAYPAL_RECEIVER_EMAIL = 'chandra2khadka4@gmail.com'
PAYPAL_TEST = True

# LOGGING = {
#     'version': 1,
#     # True if the default configuration is completely overridden
#     'disable_existing_loggers': False,
#     'formatters': {
#          'verbose': {
#              'format' :
#                  '%(asctime)s: %(name)s, line %(lineno)d: '
#                  '%(levelname)s: %(message)s ',
#              'datefmt' : "%d/%b/%Y %H:%M:%S"
#          },
#          'simple': {
#              'format': '%(levelname)s %(message)s'
#          },
#      },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue'
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         },
#
#     },
#     'handlers': {
#         'file': {
#                'level': 'DEBUG',
#                'class': 'logging.handlers.RotatingFileHandler',
#                'formatter': 'verbose',
#                'filename': os.path.join(BASE_DIR,  'log/'+datetime.datetime.now().strftime('%Y-%m-%d')+'.log'),
#                'maxBytes': 1024*1024*5, # 5Mb
#                'backupCount': 5
#            },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false']
#         },
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#         'null': {
#             "class": 'django.utils.log.NullHandler',
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins', 'console'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django': {
#             'handlers': ['null', ],
#         },
#         'django.db.backends': {
#             'handlers': ['null', ],
#             'propagate': False,
#         },
#         'py.warnings': {
#             'handlers': ['null', ],
#         },
#         '': {
#             'handlers': ['console', 'file'],
#             'level': "DEBUG",
#         },
#
#     },
# }

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

# CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
#
# CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_IMAGE_BACKEND = "pillow"
#
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': None,
#     },
# }

###################################