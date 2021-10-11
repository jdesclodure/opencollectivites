"""
Django settings for OpenCollectivités project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# Keep secrets and environment_specific variables in a separate file not using version control
from settings_local import *
from os import path
import sys
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = LOCAL_BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL_DEBUG

ALLOWED_HOSTS = LOCAL_ALLOWED_HOSTS

INTERNAL_IPS = ("127.0.0.1",)

# Application definition

INSTALLED_APPS = [
    "dsfr",
    "dashboard",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_json_widget",
    "corsheaders",
    "simple_history",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.contrib.styleguide",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "wagtailsvg",
    "wagtailmarkdown",
    "modelcluster",
    "taggit",
    "analytical",
    "francedata.apps.FrancedataConfig",
    "external_apis",
    "aspic.apps.AspicConfig",
    "core",
    "bnsp",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "config.urls"

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
                "core.context_processors.topics_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = LOCAL_DATABASES

DATABASE_ROUTERS = ["aspic.router.AspicRouter"]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = path.join(BASE_DIR, "static")

# Media files (user uploaded)
MEDIA_ROOT = path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = LOCAL_CORS_ORIGIN_WHITELIST

# Matomo
MATOMO_DOMAIN_PATH = LOCAL_MATOMO_DOMAIN_PATH
MATOMO_SITE_ID = LOCAL_MATOMO_SITE_ID

# Wagtail
WAGTAIL_SITE_NAME = "Open Collectivités — Gestion des contenus"

# Taggit
TAGGIT_CASE_INSENSITIVE = True

# Allow bulk deletions
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# Other
FRONT_HOME_URL = LOCAL_FRONT_HOME_URL
PUBLICATIONS_PER_PAGE = LOCAL_PUBLICATIONS_PER_PAGE

# Don't show logs in tests
if len(sys.argv) > 1 and sys.argv[1] == "test":
    logging.disable(logging.CRITICAL)
