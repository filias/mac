from .base import *

ALLOWED_HOSTS = ["macsiteadmin.pythonanywhere.com", "movimentoartecontemporanea.com", "www.movimentoartecontemporanea.com"]

# Email sending - gmail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "webmaster@movimentoartecontemporanea.com"
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Media files
MEDIA_URL = f"https://www.movimentoartecontemporanea.com/media/"
