# Activate Python Virtual Enviroment
activate_this = '/path/to/virtualenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
sys.path.append( os.path.abspath('%s/../../' % os.path.dirname(__file__)) )

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()