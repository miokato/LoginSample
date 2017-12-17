import os
from django.contrib.messages import constants as message_constants

import custom_settings
custom = custom_settings.load('settings_custom')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = custom.get('DJANGO_SECRET_KEY', use_environ=True, default='10bhpr$y_lgajts&pyzh(s!uf$o99roa($&z26m*enmx0sq7ql')

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

# 認証
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/workshop/' # ログインページ
LOGIN_REDIRECT_URL = '/workshop/' # ログイン後のリダイレクト先
LOGOUT_REDIRECT_URL = '/workshop/'

AUTHENTICATION_BACKENDS = [
    'accounts.models.MyAuthenticate',
    'django.contrib.auth.backends.ModelBackend',
]

MESSAGE_TAGS = {
    message_constants.SUCCESS: 'alert alert-success',
    message_constants.ERROR: 'alert alert-danger',
    message_constants.INFO: 'alert alert-info',
    message_constants.WARNING: 'alert alert-warning',
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'workshop',
    'accounts',
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
            ],
        },
    },
]
DATABASES = {
    'default': {
        'ENGINE': custom.get('DBENGINE', use_environ=True, default='django.db.backends.postgresql'),
        'HOST': custom.get('DBHOST', use_environ=True, default='localhost'),
        'NAME': custom.get('DBNAME', use_environ=True, default='postgres'),
        'USER': custom.get('DBUSER', use_environ=True, default='postgres'),
        'PASSWORD': custom.get('DBPASSWORD', use_environ=True, default='postgres'),
        'PORT': custom.get('DBPORT', use_environ=True, default=5432),
    }
}
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
