import os

from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment this for admin:
from django.contrib import admin

# Uncomment to load INSTALLED_APPS admin.py module for default AdminSite instance.
admin.autodiscover()

urlpatterns = patterns('',
    # filebrowser
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    # Uncomment this for admin docs:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment this for admin:
    #(r'^admin/(.*)', admin.site.root),
    # Static content for django server
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.BASE_DIR, "media")}),

    # i18n
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^setlang/(?P<lang_code>.*)/$', 'mac.views.set_language') , 

    (r'^mac', include('mac.galeria.urls')),
    (r'^exposicoes', include('mac.exposicoes.urls')),
    (r'^artistas', include('mac.artistas.urls')),
    (r'^publicacoes', include('mac.publicacoes.urls')),
#    (r'^servicos', 'mac.views.servicos'),
    (r'^contactos', include('mac.contactos.urls')),
    (r'^mapa', 'mac.views.mapa'),
    (r'^resultados', 'mac.views.resultados'),
    (r'^links', 'mac.views.links'),
)
