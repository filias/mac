from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from filebrowser.sites import site

from .views import links, mapa, resultados

admin.autodiscover()

urlpatterns = [
    path("admin/filebrowser/", site.urls),
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),

    # Static content for django server (only used for development)
    #path(
    #    "static/(?P<path>.*)$",
    #    serve,
    #    {"document_root": settings.PROJECT_ROOT / "static"},
    #),

    # i18n
    url(r"^i18n/", include("django.conf.urls.i18n")),

    # Site urls
    path("mac/", include("mac.gallery.urls")),
    path("artistas/", include("mac.art.urls")),
    path("mapa/", mapa),
    path("resultados/", resultados),
    path("links/", links),
]
