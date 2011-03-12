from django.conf.urls.defaults import *

urlpatterns = patterns('mac.publicacoes.views',
    (r'^$', 'index'),
    (r'^/newsletters/(?P<select>\w+)/$', 'newsletters'),
    (r'^/catalogos/(?P<select>\w+)/$', 'catalogos'),
    (r'^/monografias/(?P<select>\w+)/$', 'monografias'),
    (r'^/imprensa/(?P<select>\w+)/$', 'imprensa'),
    (r'^/critica/(?P<select>\w+)/$', 'critica'),
)
