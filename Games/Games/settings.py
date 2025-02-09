from pathlib import Path
from datetime import timedelta

from .DataBase_Config import DATABASES_CONFIG

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path ( __file__ ).resolve ( ).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-()t73wz!-qtr)exz+2vyvet6kub)tmlmjj^0e*=q70#zf=ux8n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin' ,
    'django.contrib.auth' ,
    'django.contrib.contenttypes' ,
    'django.contrib.sessions' ,
    'django.contrib.messages' ,
    'django.contrib.staticfiles' ,
    'Games_app.apps.GamesAppConfig' ,
    'rest_framework' ,
    'drf_yasg' ,
    'django_filters',
    'corsheaders',
    'djoser' ,

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware' ,
    'django.contrib.sessions.middleware.SessionMiddleware' ,
    'django.middleware.common.CommonMiddleware' ,
    'django.middleware.csrf.CsrfViewMiddleware' ,
    'django.contrib.auth.middleware.AuthenticationMiddleware' ,
    'django.contrib.messages.middleware.MessageMiddleware' ,
    'django.middleware.clickjacking.XFrameOptionsMiddleware' ,
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [  # Разрешённые домены
    "http://localhost:3000" ,  # Если фронт на React
    "http://127.0.0.1:8000" ,  # Если тестируем в браузере
]
AUTH_USER_MODEL = 'auth.User'
ROOT_URLCONF = 'Games.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates' ,
        'DIRS' : [ ] ,
        'APP_DIRS' : True ,
        'OPTIONS' : {
            'context_processors' : [
                'django.template.context_processors.debug' ,
                'django.template.context_processors.request' ,
                'django.contrib.auth.context_processors.auth' ,
                'django.contrib.messages.context_processors.messages' ,
            ] ,
        } ,
    } ,
]

WSGI_APPLICATION = 'Games.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = DATABASES_CONFIG

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME' : 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' ,
    } ,
    {
        'NAME' : 'django.contrib.auth.password_validation.MinimumLengthValidator' ,
    } ,
    {
        'NAME' : 'django.contrib.auth.password_validation.CommonPasswordValidator' ,
    } ,
    {
        'NAME' : 'django.contrib.auth.password_validation.NumericPasswordValidator' ,
    } ,
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS' : 'rest_framework.schemas.coreapi.AutoSchema' ,
                   'DEFAULT_FILTER_BACKENDS' : [ 'django_filters.rest_framework.DjangoFilterBackend' ] ,
                   'DEFAULT_AUTHENTICATION_CLASSES' : (
                       'rest_framework_simplejwt.authentication.JWTAuthentication' ,
                   ) ,
                   }
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
