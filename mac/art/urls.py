from django.urls import path

from .views import *

urlpatterns = [
    path("", artists, name="artists"),
    path("<int:artist_id>/", detail, name="artist_detail"),
    path("<int:artist_id>/obras/", works, name="artist_works"),
    path("<int:artist_id>/obras/<int:obra_id>/", work_detail, name="work_detail"),
    path("<int:artist_id>/acervo/", collection, name="artist_collection"),
    path("<int:artist_id>/exposicoes/", exhibitions, name="artist_exhibitions"),
    path("<int:artist_id>/critica/", critics, name="artist_critics"),
    path("<int:artist_id>/imprensa/", press, name="artist_press"),
]
