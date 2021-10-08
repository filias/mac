from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^$", index, name="gallery"),
    url(r"^galerias$", galerias, name="galleries"),
    url(r"^missao/$", missao, name="mission"),
    url(r"^historia/$", historia, name="history"),
    url(r"^curriculum/$", curriculum, name="curriculum"),
    url(r"^curriculum/(?P<evento_ano>\d+)/$", curriculum_ano, name="curriculum_year"),
    url(r"^equipa/$", equipa, name="team"),
    url(r"^acervo/$", acervo, name="collection"),
    url(r"^acervo/(?P<artist_id>\d+)/$", acervo_artist, name="collection_by_artist"),
    url(
        r"^acervo/(?P<artist_id>\d+)/(?P<obra_id>\d+)/$",
        acervo_detalhe,
        name="collection_detail",
    ),
    url(r"^agenda/$", agenda, name="calendar"),
    url(r"^premios/$", premios, name="awards"),
    url(r"^premios/(?P<aniversario_id>\d+)/$", detail, name="anniversary_detail"),
    url(
        r"^premios/(?P<aniversario_id>\d+)/premiados/$",
        premiados,
        name="anniversary_prizes",
    ),
    url(r"^premios/(?P<aniversario_id>\d+)/trofeu$", trofeu, name="anniversary_trophy"),
    url(r"^tela", tela, name="banner"),
    url(r"^actuais/$", index, name="current_exhibitions"),
    url(r"^passadas/$", passadas, name="past_exhibitions"),
    url(r"^futuras/$", futuras, name="future_exhibitions"),
    url(
        r"^passadas/(?P<exposicao_ano>\d+)/$",
        passadas_ano,
        name="past_exhibitions_per_year",
    ),
    url(r"^(?P<exposicao_id>\d+)/$", detail, name="exhibition_detail"),
    url(r"^(?P<exposicao_id>\d+)/obras/$", obras, name="exhibition_works"),
    url(
        r"^(?P<exposicao_id>\d+)/obras/(?P<obra_id>\d+)/$",
        obra_detalhe,
        name="work_detail",
    ),
    url(r"^$", contactos, name="contacts"),
    url(r"^contacte_nos/$", contacte_nos, name="contact_us"),
    url(r"^contacte_nos/sucesso/$", sucesso, name="contact_success"),
    url(r"^catalogos/(?P<select>\w+)/$", catalogos, name="catalogs"),
    url(r"^imprensa/(?P<select>\w+)/$", imprensa, name="press"),
    url(r"^critica/(?P<select>\w+)/$", critica, name="critics"),
]
