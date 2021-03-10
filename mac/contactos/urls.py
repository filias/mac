from django.conf.urls.defaults import *

urlpatterns = patterns('mac.contactos.views',
    (r'^$', 'contactos'),
    (r'^/contacte_nos/$', 'contacte_nos'),
    (r'^/contacte_nos/sucesso/$', 'sucesso'),
)


