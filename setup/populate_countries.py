import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django_countries import countries
from countries_app.models import Country

countries_dict = dict(countries)

for country in countries_dict.values():
    Country(name=country).save()