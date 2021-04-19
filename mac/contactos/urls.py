from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^$", contactos, name="contacts"),
    url(r"^contacte_nos/$", contacte_nos, name="contact_us"),
    url(r"^contacte_nos/sucesso/$", sucesso, name="contact_success"),
]
