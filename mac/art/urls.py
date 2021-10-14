from django.urls import path

from .views import *

urlpatterns = [
    path("", artistas, name="artists"),
    path("(<int:artist_id>)/", detail, name="artist_detail"),
    path("(<int:artist_id>)/obras/", obras, name="artist_works"),
    path("(<int:artist_id>)/obras/(<int:obra_id>)/", obra_detalhe, name="work_detail"),
    path("(<int:artist_id>)/acervo/", acervo, name="artist_collection"),
    path("(<int:artist_id>)/exposicoes/", exposicoes, name="artist_exhibitions"),
    path("(<int:artist_id>)/critica/", critica, name="artist_critics"),
    path("(<int:artist_id>)/imprensa/", imprensa, name="artist_press"),
]
