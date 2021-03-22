from django.conf.urls import patterns


urlpatterns = patterns('mac.contactos.views',
    (r'^$', 'contactos'),
    (r'^/contacte_nos/$', 'contacte_nos'),
    (r'^/contacte_nos/sucesso/$', 'sucesso'),
)


