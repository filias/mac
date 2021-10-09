from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from filebrowser.sites import site

from .gallery.views import (
    catalogos,
    contacte_nos,
    contactos,
    critica,
    detail,
    exhibitions,
    futuras,
    imprensa,
    obra_detalhe,
    obras,
    passadas,
    passadas_ano,
    sucesso,
)
from .views import links, mapa, resultados

admin.autodiscover()

urlpatterns = [
    path("admin/filebrowser/", site.urls),
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    # Static content for django server (only used for development)
    # path(
    #    "static/(?P<path>.*)$",
    #    serve,
    #    {"document_root": settings.PROJECT_ROOT / "static"},
    # ),
    # i18n
    url(r"^i18n/", include("django.conf.urls.i18n")),
    # Site urls
    path("mac/", include("mac.gallery.urls")),
    path("art/", include("mac.art.urls")),
    path("mapa/", mapa),
    path("resultados/", resultados),
    path("links/", links),
    # Exhibitions
    url(r"^exposicoes/actuais/$", exhibitions, name="current_exhibitions"),
    url(r"^exposicoes/passadas/$", passadas, name="past_exhibitions"),
    url(r"^exposicoes/futuras/$", futuras, name="future_exhibitions"),
    url(
        r"^exposicoes/passadas/(?P<exposicao_ano>\d+)/$",
        passadas_ano,
        name="past_exhibitions_per_year",
    ),
    url(r"^exposicoes/(?P<exposicao_id>\d+)/$", detail, name="exhibition_detail"),
    url(r"^exposicoes/(?P<exposicao_id>\d+)/obras/$", obras, name="exhibition_works"),
    url(
        r"^exposicoes/(?P<exposicao_id>\d+)/obras/(?P<obra_id>\d+)/$",
        obra_detalhe,
        name="work_detail",
    ),
    # Contacts
    url(r"^contactos/", contactos, name="contacts"),
    url(r"^contacte_nos/$", contacte_nos, name="contact_us"),
    url(r"^contacte_nos/sucesso/$", sucesso, name="contact_success"),
    # Publications
    url(r"^publicacoes/catalogos/(?P<select>\w+)/$", catalogos, name="catalogs"),
    url(r"^publicacoes/imprensa/(?P<select>\w+)/$", imprensa, name="press"),
    url(r"^publicacoes/critica/(?P<select>\w+)/$", critica, name="critics"),
]
