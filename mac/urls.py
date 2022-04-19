from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from filebrowser.sites import site

from .gallery.views import (
    contacte_nos,
    contactos,
    detail,
    exhibitions,
    work_detail,
    exhibition_works,
    past_by_year,
    publications,
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
    path("artists/", include("mac.art.urls")),
    path("mapa/", mapa),
    path("resultados/", resultados),
    path("links/", links),

    # Exhibitions
    path("exposicoes/", exhibitions, name="exhibitions"),
    path(
        "exposicoes/passadas/<int:exposicao_ano>/",
        past_by_year,
        name="past_exhibitions_per_year",
    ),
    path("exposicoes/<int:exposicao_id>/", detail, name="exhibition_detail"),
    path("exposicoes/<int:exposicao_id>/obras/", exhibition_works, name="exhibition_works"),
    path(
        "exposicoes/<int:exposicao_id>/obras/<int:obra_id>/",
        work_detail,
        name="work_detail",
    ),

    # Contacts
    path("contactos/", contactos, name="contacts"),
    path("contacte_nos/", contacte_nos, name="contact_us"),
    path("contacte_nos/sucesso/", sucesso, name="contact_success"),

    # Publications
    path("publicacoes/", publications, name="publications"),
]
