from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import VenueForm, EventForm, ConsultantForm
from django.http import HttpResponseRedirect
from .models import *


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # convert month from name to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    # get current year
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M')

    return render(request,
                  'events/home.html', {
                      'year': year, 'month': month,
                      'cal': cal,
                      'current_year': current_year, 'time': time,
                  })


# *************CONSULTANTS
def add_consultant(request):
    submitted = False
    if request.method == 'POST':
        form = ConsultantForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/add_consultant?submitted=True')
    else:
        form = ConsultantForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_consultant.html', {'form': form, 'submitted': submitted})


def list_consultants(request):
    consultant_list = Consultant.objects.all()
    return render(request, 'events/consultants.html', {'consultant_list': consultant_list})


def update_consultant(request, consultant_id):
    consultant = Consultant.objects.get(pk=consultant_id)
    form = ConsultantForm(request.POST or None, instance=consultant)
    if form.is_valid():
        form.save()
        return redirect('list_consultants')
    return render(request, 'events/update_consultant.html', {'consultant': consultant, 'form': form})


# *************EVENTS
def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def list_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list_events')
    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list_events')


def search_events(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = Event.objects.filter(description__contains=searched)

        return render(request,
                      'events/search_events.html',
                      {'searched': searched,
                       'events': events})
    else:
        return render(request,
                      'events/search_events.html',
                      {})


# ******VENUES
def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', {'venue_list': venue_list})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list_venues')
    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


# Delete a Venue
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list_venues')


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})
