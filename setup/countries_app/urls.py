from django.urls import path
from .views import (
    homepage,
    add_trip,
    trip,
    add_comment,
    search_country,
)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_trip/', add_trip, name='add_trip'),
    path('trips/<int:country_id>', trip, name='trip'),
    path('add_comment/<int:country_id>', add_comment, name='add_comment'),
    path('search_country', search_country, name='search_country'),
]