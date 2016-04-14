import os, sys
# Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

# Add the path to 3rd party django application and to django itself.
sys.path.append('/home/nhla')
sys.path.append('/usr/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/dist-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'GoldStandardWeb.apache.override'


try:
  from django.core.wsgi import get_wsgi_application
  application = get_wsgi_application()
except Exception:
    print 'handling WSGI exception'
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
