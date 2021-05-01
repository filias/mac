import os

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from filebrowser.sites import site

from .views import links, mapa, resultados

admin.autodiscover()

urlpatterns = [
    url(r"^admin/filebrowser/", site.urls),
    url(r"^grappelli/", include("grappelli.urls")),
    url(r"^admin/", admin.site.urls),
    # Static content for django server (only used for development)
    url(
        r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.PROJECT_ROOT / "static"},
    ),
    # i18n
    url(r"^i18n/", include("django.conf.urls.i18n")),
    # Site urls
    url(r"^mac/", include("mac.galeria.urls")),
    url(r"^exposicoes/", include("mac.exposicoes.urls")),
    url(r"^artistas/", include("mac.artistas.urls")),
    url(r"^publicacoes/", include("mac.publicacoes.urls")),
    url(r"^geral/", include("mac.geral.urls")),
    url(r"^mapa/", mapa),
    url(r"^resultados/", resultados),
    url(r"^links/", links),
]
