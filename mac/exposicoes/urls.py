from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^actuais/$', index),
    url(r'^passadas/$', passadas),
    url(r'^futuras/$', futuras),
    url(r'^passadas/(?P<exposicao_ano>\d+)/$', passadas_ano),
    url(r'^(?P<exposicao_id>\d+)/$', detail),
    url(r'^(?P<exposicao_id>\d+)/obras/$', obras),
    url(r'^(?P<exposicao_id>\d+)/obras/(?P<obra_id>\d+)/$', obra_detalhe),
]
