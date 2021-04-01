from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', contactos),
    url(r'^contacte_nos/$', contacte_nos),
    url(r'^contacte_nos/sucesso/$', sucesso),
]
