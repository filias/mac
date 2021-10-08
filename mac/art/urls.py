from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^$", artistas, name="artists"),
    url(r"^pintura/$", pintura, name="painting"),
    url(r"^joalharia/$", joalharia, name="jewelry"),
    url(r"^escultura/$", escultura, name="sculpture"),
    url(r"^fotografia/$", fotografia, name="photography"),
    url(r"^desenho/$", desenho, name="drawing"),
    url(r"^ceramica/$", ceramica, name="ceramics"),
    url(r"^medalhistica/$", medalhistica, name="medals"),
    url(r"^(?P<artist_id>\d+)/$", detail, name="artist_detail"),
    url(r"^(?P<artist_id>\d+)/obras/$", obras, name="artist_works"),
    url(
        r"^(?P<artist_id>\d+)/obras/(?P<obra_id>\d+)/$",
        obra_detalhe,
        name="work_detail",
    ),
    url(r"^(?P<artist_id>\d+)/acervo/$", acervo, name="artist_collection"),
    url(r"^(?P<artist_id>\d+)/exposicoes/$", exposicoes, name="artist_exhibitions"),
    url(r"^(?P<artist_id>\d+)/critica/$", critica, name="artist_critics"),
    url(r"^(?P<artist_id>\d+)/imprensa/$", imprensa, name="artist_press"),
]
