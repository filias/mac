from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^catalogos/(?P<select>\w+)/$", catalogos, name="catalogs"),
    url(r"^imprensa/(?P<select>\w+)/$", imprensa, name="press"),
    url(r"^critica/(?P<select>\w+)/$", critica, name="critics"),
]
