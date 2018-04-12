import sys
import os
sys.path.append('/home/pansek/webserver')
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'webserver.settings'
django.setup()

from source.models import Searching_Detail as SD

i = 0
for obj in SD.objects.filter(account__email='pan@ptt.com'):
    i+=1

print('count = ' + str(i))
