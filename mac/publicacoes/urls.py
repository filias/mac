from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^$", index),
    url(r"^newsletters/(?P<select>\w+)/$", newsletters),
    url(r"^catalogos/(?P<select>\w+)/$", catalogos),
    url(r"^monografias/(?P<select>\w+)/$", monografias),
    url(r"^imprensa/(?P<select>\w+)/$", imprensa),
    url(r"^critica/(?P<select>\w+)/$", critica),
]
