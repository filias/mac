# Django settings for mac project.

DEBUG = True
#TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Filipa Andrade', 'admin@movimentoartecontemporanea.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'alvarogomes_mac'             # Or path to database file if using sqlite3.
DATABASE_USER = 'alvarogomes_mac'             # Not used with sqlite3.
DATABASE_PASSWORD = 'mac_pass'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Lisbon'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-pt'
LANGUAGES = (
    ('en', 'English'),
    ('pt', 'Portuguese'),
)
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/alvarogomes/webapps/django_media/'
#MEDIA_ROOT = '/home/filipa/programming/websites/mac/django-media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w-ezr04of=m-vsp0om4b-dq7lkqqdf39gucpvs@gmi^@@q8hye'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware', 
)

ROOT_URLCONF = 'mac.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    "/home/filipa/programming/websites/mac"
    "/home/alvarogomes/webapps/django/mac",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.redirects', 
    'mac.galeria',
    'mac.exposicoes',
    'mac.artistas',
    'mac.publicacoes',
    'mac.contactos',
    'mac.geral',
    'filebrowser',
)

# for webfaction
#EMAIL_HOST = 'mail3.webfaction.com'
#for gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'webmaster@movimentoartecontemporanea.com'
EMAIL_HOST_PASSWORD = 'webmacpass'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
