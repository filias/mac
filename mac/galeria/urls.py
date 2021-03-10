from django.conf.urls.defaults import *

urlpatterns = patterns('mac.galeria.views',
    (r'^/$', 'index'),
    (r'^/galerias$', 'galerias'),
    (r'^/missao/$', 'missao'),
    (r'^/historia/$', 'historia'),
    (r'^/curriculum/$', 'curriculum'),
    (r'^/curriculum/(?P<evento_ano>\d+)/$', 'curriculum_ano'),
    (r'^/equipa/$', 'equipa'),
    (r'^/acervo/$', 'acervo'),
    (r'^/acervo/(?P<artist_id>\d+)/$', 'acervo_artist'),
    (r'^/acervo/(?P<artist_id>\d+)/(?P<obra_id>\d+)/$', 'acervo_detalhe'),
    (r'^/visita/$', 'visita'),
    (r'^/agenda/$', 'agenda'),
    (r'^/premios/$', 'premios'),
    (r'^/premios/(?P<aniversario_id>\d+)/$', 'detail'),
    (r'^/premios/(?P<aniversario_id>\d+)/premiados/$', 'premiados'),
    (r'^/premios/(?P<aniversario_id>\d+)/trofeu$', 'trofeu'),
    (r'^/tela', 'tela'),
)

