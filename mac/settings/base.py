import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
PROJECT_ROOT = Path(__file__).parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "mac"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": "",
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Lisbon"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = "pt-pt"
LANGUAGES = (
    ("en", "English"),
    ("pt", "Portuguese"),
)

LOCALE_PATHS = [PROJECT_ROOT / "locale"]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# aws settings for media
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"

# Static files settings
STATICFILES_DIRS = [PROJECT_ROOT / "static"]
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "mac.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_ROOT],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mac.geral.context_processors.contacts_renderer",
                "mac.geral.context_processors.telas_renderer",
            ),
            "debug": False,
        },
    },
]

INSTALLED_APPS = (
    "grappelli",
    "filebrowser",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.redirects",
    "django.contrib.staticfiles",
    "mac.galeria",
    "mac.exposicoes",
    "mac.artistas",
    "mac.publicacoes",
    "mac.geral",
    "storages",
)
