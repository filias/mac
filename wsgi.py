# import os
# import sys
# os.environ['DJANGO_SETTINGS_MODULE'] = 'filebrowser.settings'
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "mac.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
