from pathlib import Path
from datetime import timedelta
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")

DEBUG = True

ALLOWED_HOSTS=['*']

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_rest_passwordreset',
    'rest_framework_simplejwt',
    'PerformanceTab',
    'loginAPI',
    'corsheaders',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'Employees',
    'Plan',
    'Projects',
    'Invoicing',
    'RevenueCosts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'GhostProjectBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'GhostProjectBackend.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': env("NAME"),
    'USER': env("USER"),
    'PASSWORD': env("PASSWORD"),
    'HOST': 'localhost',
    'PORT': '3306',
  }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
}

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("SIFRA")
EMAIL_USE_SSL = True





