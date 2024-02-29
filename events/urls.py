from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('add_venue/', add_venue, name='add_venue'),
    path('list_venues/', list_venues, name='list_venues'),
    path('update_venue/<venue_id>', update_venue, name='update_venue'),
    path('delete_venue/<venue_id>', delete_venue, name='delete_venue'),
    path('show_venue/<venue_id>', show_venue, name='show_venue'),
    path('venue_events/<venue_id>', venue_events, name='venue_events'),
    path('search_venues', search_venues, name='search_venues'),

    path('add_consultant/', add_consultant, name='add_consultant'),
    path('list_consultants/', list_consultants, name='list_consultants'),
    path('update_consultant/', update_consultant, name='update_consultant'),
    path('delete_consultant/', delete_consultant, name='delete_consultant'),
    path('show_consultant/', show_consultant, name='show_consultant'),

    path('add_event/', add_event, name='add_event'),
    path('add_events/', add_events, name='add_events'),
    path('all_events/', all_events, name='all_events'),
    path('list_events/', list_events, name='list_events'),
    path('show_event/<event_id>', show_event, name='show_event'),
    path('delete_event/<event_id>', delete_event, name='delete_event'),
    path('update_event/<event_id>', update_event, name='update_event'),
    path('update/', update, name='update'),
    path('remove/', remove, name='remove'),
    path('admin_approval/', admin_approval, name='admin_approval'),

    path('add_cons_course/', add_cons_course, name='add_cons_course'),
    path('list_cons_course/', list_cons_course, name='list_cons_course'),
    path('update_cons_course/', update_cons_course, name='update_cons_course'),

    path('list_courses/', list_courses, name='list_courses'),
    path('list_certificates/', list_certificates, name='list_certificates'),





]
