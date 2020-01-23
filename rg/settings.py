# -*- coding: utf-8 -*-

""" settings """

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "+*6x!0^!j^&h4+l-w7h!)pk=1m7gie&@&0cjq7)19%d6v2xu=y"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG"))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development" if DEBUG else "production")
READ_ONLY = ENVIRONMENT == "production"

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    "[::1]",
    "localhost",
    ".recommend.games",
    ".recommended.games",
]

if DEBUG:
    ALLOWED_HOSTS += [".local"]

if os.getenv("GC_PROJECT"):
    ALLOWED_HOSTS += [f".{os.getenv('GC_PROJECT')}.appspot.com"]

# Application definition

INSTALLED_APPS = [
    "rest_framework",
    "django_filters",
    "games.apps.GamesConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]

if DEBUG:
    INSTALLED_APPS.append("django.contrib.admin")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rg.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "rg.wsgi.application"

SECURE_SSL_REDIRECT = bool(os.getenv("SECURE_SSL_REDIRECT"))
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(DATA_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/"
STATIC_ROOT = os.path.join(BASE_DIR, "app" if DEBUG else "static")
STATICFILES_DIRS = [] if DEBUG else [os.path.join(BASE_DIR, ".temp")]
STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.StaticFilesStorage"
    if DEBUG
    else "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# WhiteNoise

WHITENOISE_INDEX_FILE = True

# REST framework

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}

# REST proxy
REST_PROXY = {"HOST": "http://news.recommend.games"}

# Custom

RECOMMENDER_PATH = os.path.join(DATA_DIR, "recommender_bgg")
BGA_RECOMMENDER_PATH = os.path.join(DATA_DIR, "recommender_bga")
STAR_PERCENTILES = (0.165, 0.365, 0.615, 0.815, 0.915, 0.965, 0.985, 0.995)

PUBSUB_PUSH_ENABLED = True
PUBSUB_QUEUE_PROJECT = os.getenv("PUBSUB_QUEUE_PROJECT") or os.getenv("GC_PROJECT")
PUBSUB_QUEUE_TOPIC = os.getenv("PUBSUB_QUEUE_TOPIC")

MODEL_UPDATED_FILE = os.path.join(DATA_DIR, "updated_at")
PROJECT_VERSION_FILE = os.path.join(BASE_DIR, "VERSION")
