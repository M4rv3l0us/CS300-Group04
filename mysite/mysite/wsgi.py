import os
import sys
sys.path.append(r'D:\My stuffs\Software Engineering\mysite\mysite')
from django.core.wsgi import get_wsgi_application
from WSGI.application import MyApplication
#os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

application = get_wsgi_application() # call in mysite.wsgi.application
application = MyApplication(application)