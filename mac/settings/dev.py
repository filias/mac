from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG
