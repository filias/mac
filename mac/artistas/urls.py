from django.conf.urls import patterns


urlpatterns = patterns('mac.artistas.views',
    (r'^$', 'artistas'),
    (r'^/pintura/$', 'pintura'),
    (r'^/joalharia/$', 'joalharia'),
    (r'^/escultura/$', 'escultura'),
    (r'^/fotografia/$', 'fotografia'),
    (r'^/desenho/$', 'desenho'),
    (r'^/ceramica/$', 'ceramica'),
    (r'^/medalhistica/$', 'medalhistica'),
    (r'^/(?P<artist_id>\d+)/$', 'detail'),
    (r'^/(?P<artist_id>\d+)/obras/$', 'obras'),
    (r'^/(?P<artist_id>\d+)/obras/(?P<obra_id>\d+)/$', 'obra_detalhe'),
    (r'^/(?P<artist_id>\d+)/acervo/$', 'acervo'),
    (r'^/(?P<artist_id>\d+)/exposicoes/$', 'exposicoes'),
    (r'^/(?P<artist_id>\d+)/critica/$', 'critica'),
    (r'^/(?P<artist_id>\d+)/imprensa/$', 'imprensa'),
)


