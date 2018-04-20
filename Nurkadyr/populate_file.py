import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Nurkadyr.settings')

import django
django.setup()

from faker import Faker

fakegen =Faker()
