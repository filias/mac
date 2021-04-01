from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', artistas),
    url(r'^pintura/$', pintura),
    url(r'^joalharia/$', joalharia),
    url(r'^escultura/$', escultura),
    url(r'^fotografia/$', fotografia),
    url(r'^desenho/$', desenho),
    url(r'^ceramica/$', ceramica),
    url(r'^medalhistica/$', medalhistica),
    url(r'^(?P<artist_id>\d+)/$', detail),
    url(r'^(?P<artist_id>\d+)/obras/$', obras),
    url(r'^(?P<artist_id>\d+)/obras/(?P<obra_id>\d+)/$', obra_detalhe),
    url(r'^(?P<artist_id>\d+)/acervo/$', acervo),
    url(r'^(?P<artist_id>\d+)/exposicoes/$', exposicoes),
    url(r'^(?P<artist_id>\d+)/critica/$', critica),
    url(r'^(?P<artist_id>\d+)/imprensa/$', imprensa),
]
