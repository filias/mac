import os

from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Static content for django server
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.BASE_DIR, "static")}),
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.BASE_DIR, "media")}),

    # i18n
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^setlang/(?P<lang_code>.*)/$', 'mac.views.set_language'),

    (r'^mac', include('mac.galeria.urls')),
    (r'^exposicoes', include('mac.exposicoes.urls')),
    (r'^artistas', include('mac.artistas.urls')),
    (r'^publicacoes', include('mac.publicacoes.urls')),
    (r'^contactos', include('mac.contactos.urls')),
    (r'^mapa', 'mac.views.mapa'),
    (r'^resultados', 'mac.views.resultados'),
    (r'^links', 'mac.views.links'),
)
