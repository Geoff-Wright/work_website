from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:year>/<str:month>/', home, name='home'),
    path('add_venue', add_venue, name='add_venue'),
    path('list_venues', list_venues, name='list_venues'),
    path('show_venue/<venue_id>', show_venue, name='show_venue'),
    path('search_venues', search_venues, name='search_venues'),
    path('update_venue/<venue_id>', update_venue, name='update_venue'),
    path('delete_venue/<venue_id>', delete_venue, name='delete_venue'),

    path('add_event', add_event, name='add_event'),
    path('list_events', list_events, name='list_events'),
    path('update_event/<event_id>', update_event, name='update_event'),
    path('my_events', add_event, name='my_events'),
    path('search_events', search_events, name='search_events'),
    path('delete_event/<event_id>', delete_event, name='delete-event'),

    path('add_consultant', add_consultant, name='add_consultant'),
    path('list_consultants', list_consultants, name='list_consultants'),
    path('update_consultant/<consultant_id>', update_consultant, name='update_consultant'),
]
