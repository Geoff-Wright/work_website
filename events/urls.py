from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # full cal only
    # path('', home, name='home'), small cal only
    # path('<int:year>/<str:month>/', home, name='home'), small cal only
    path('add_venue', add_venue, name='add_venue'),
    path('list_venues', list_venues, name='list_venues'),
    path('update_venue/<venue_id>', update_venue, name='update_venue'),
    path('delete_venue/<venue_id>', delete_venue, name='delete_venue'),
    path('search_venues', search_venues, name='search_venues'),
    path('show_venue/<venue_id>', show_venue, name='show_venue'),

    path('all_events/', all_events, name='all_events'),
    path('show_event/<event_id>', show_event, name='show_event'),
    path('list_events/', list_events, name='list_events'),
    path('list_courses/', list_courses, name='list_courses'),
    path('list_certificates/', list_certificates, name='list_certificates'),
    path('add_event/', add_event, name='add_event'),
    path('add_events/', add_events, name='add_events'),
    path('delete_event/<event_id>', delete_event, name='delete_event'),
    path('update_event/<event_id>', update_event, name='update_event'),
    path('update/', update, name='update'),
    path('remove/', remove, name='remove'),

    path('add_consultant', add_consultant, name='add_consultant'),
    path('list_consultants', list_consultants, name='list_consultants'),
    path('update_consultant/<consultant_id>', update_consultant, name='update_consultant'),
    path('delete_consultant/<consultant_id>', delete_consultant, name='delete_consultant'),
    path('show_consultant/<consultant_id>', show_consultant, name='show_consultant'),
]
