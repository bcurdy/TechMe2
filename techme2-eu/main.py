import logging, os

os.environ['DJANGO_SETTINGS_MODULE'] = 'podcast.settings'
from google.appengine.dist import use_library
use_library('django', '1.1')

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.import logging, os

os.environ['DJANGO_SETTINGS_MODULE'] = 'podcast.settings'
from google.appengine.dist import use_library
use_library('django', '1.1')

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

# Must set this env var + import before importing any part of Django
# 'podcast' is the name of the project created with django-admin.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'podcast.settings'

#Django imports
import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch

def log_exception(*args, **kwds):
    logging.exception('Exception in request:')

# Log errors.
error_signal = django.dispatch.Signal()
error_signal.connect(log_exception, django.core.signals.got_request_exception)

# Unregister the rollback event handler.
# django.dispatch.dispatcher.disconnect(
#    django.db._rollback_on_exception,
#    django.core.signals.got_request_exception)

def main():
    # Create a Django application for WSGI.
    application = django.core.handlers.wsgi.WSGIHandler()

    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()