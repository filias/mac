from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="gallery"),
    path("galerias", galerias, name="galleries"),
    path("missao/", missao, name="mission"),
    path("historia/", historia, name="history"),
    path("curriculum/", curriculum, name="curriculum"),
    path("curriculum/<int:evento_ano>/", curriculum_ano, name="curriculum_year"),
    path("equipa/", equipa, name="team"),
    path("acervo/", acervo, name="collection"),
    path("acervo/<int:artist_id>", acervo_artist, name="collection_by_artist"),
    path(
        "obras/<int:obra_id>/",
        acervo_detalhe,
        name="collection_detail",
    ),
    path("agenda/", agenda, name="calendar"),
    path("premios/", premios, name="awards"),
    path("premios/<int:aniversario_id>/", anniversary_detail, name="anniversary_detail"),
    path(
        "premios/<int:aniversario_id>/premiados/",
        premiados,
        name="anniversary_prizes",
    ),
    path("premios/<int:aniversario_id>/trofeu", trofeu, name="anniversary_trophy"),
    path("tela", tela, name="banner"),
]
