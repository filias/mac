from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^$", index),
    url(r"^catalogos/(?P<select>\w+)/$", catalogos),
    url(r"^imprensa/(?P<select>\w+)/$", imprensa),
    url(r"^critica/(?P<select>\w+)/$", critica),
]
