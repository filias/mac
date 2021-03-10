from django.conf.urls.defaults import *

urlpatterns = patterns('mac.exposicoes.views',
    (r'^/actuais/$', 'index'),
    (r'^/passadas/$', 'passadas'),
    (r'^/futuras/$', 'futuras'),
    (r'^/passadas/(?P<exposicao_ano>\d+)/$', 'passadas_ano'),
    (r'^/(?P<exposicao_id>\d+)/$', 'detail'),
    (r'^/(?P<exposicao_id>\d+)/obras/$', 'obras'),
    (r'^/(?P<exposicao_id>\d+)/obras/(?P<obra_id>\d+)/$', 'obra_detalhe'),
)
