from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^galerias$', galerias),
    url(r'^missao/$', missao),
    url(r'^historia/$', historia),
    url(r'^curriculum/$', curriculum),
    url(r'^curriculum/(?P<evento_ano>\d+)/$', curriculum_ano),
    url(r'^equipa/$', equipa),
    url(r'^acervo/$', acervo),
    url(r'^acervo/(?P<artist_id>\d+)/$', acervo_artist),
    url(r'^acervo/(?P<artist_id>\d+)/(?P<obra_id>\d+)/$', acervo_detalhe),
    url(r'^visita/$', visita),
    url(r'^agenda/$', agenda),
    url(r'^premios/$', premios),
    url(r'^premios/(?P<aniversario_id>\d+)/$', detail),
    url(r'^premios/(?P<aniversario_id>\d+)/premiados/$', premiados),
    url(r'^premios/(?P<aniversario_id>\d+)/trofeu$', trofeu),
    url(r'^tela', tela),
]
