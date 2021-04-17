from django.conf.urls import url

from .views import *

urlpatterns = [
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
]
