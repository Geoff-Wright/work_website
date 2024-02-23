from django.shortcuts import render, redirect
from .forms import VenueForm, EventForm, ConsultantForm, ConsCourseForm
from django.http import HttpResponseRedirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages


def my_events(request):
    if request.user.is_authenticated:
        me = request.user.id
        events = Event.objects.filter(attendees=me)
        return render(request,
                      'events/my_events.html', {
                          "events": events
                      })

    else:
        messages.success(request, "You Aren't Authorized To View This Page")
        return redirect('index')


# Create Admin Event Approval Page
def admin_approval(request):
    # Get The Venues
    venue_list = Venue.objects.all()
    # Get Counts
    event_count = Event.objects.all().count()
    venue_count = Venue.objects.all().count()
    user_count = User.objects.all().count()

    event_list = Event.objects.all().order_by('-event_date')
    if request.user.is_superuser:
        if request.method == "POST":
            # Get list of checked box id's
            id_list = request.POST.getlist('boxes')
            # Uncheck all events
            event_list.update(approved=False)
            # Update the database
            for x in id_list:
                Event.objects.filter(pk=int(x)).update(approved=True)
            # Show Success Message and Redirect
            messages.success(request, "Event List Approval Has Been Updated!")
            return redirect('list-events')
        else:
            return render(request, 'events/admin_approval.html',
                          {"event_list": event_list,
                           "event_count": event_count,
                           "venue_count": venue_count,
                           "user_count": user_count,
                           "venue_list": venue_list})
    else:
        messages.success(request, "You aren't authorized to view this page!")
        return redirect('index')

    return render(request, 'events/admin_approval.html')


def list_cons_course(request):
    cons_course_list = Cons_Course.objects.order_by("consultant")
    return render(request, 'events/cons_course.html', {'cons_course_list': cons_course_list})


def update_cons_course(request):
    cons_course = Consultant.objects.get(pk=8)
    form = ConsCourseForm(request.POST or None, instance=cons_course)
    if form.is_valid():
        form.save()
        return redirect('list_cons_course')
    return render(request, 'events/update_cons_course.html', {'cons_course': cons_course, 'form': form})


def delete_cons_course(request, cons_course_id):
    cons_course = Cons_Course.objects.get(pk=cons_course_id)
    cons_course.delete()
    return redirect('consultants')


def add_cons_course(request):
    submitted = False
    if request.method == 'POST':
        form = ConsCourseForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/add_cons_course?submitted=True')
    else:
        form = ConsCourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_cons_course.html', {'form': form, 'submitted': submitted})


def list_courses(request):
    course_list = Course.objects.all()
    return render(request, 'events/courses.html', {'course_list': course_list})


def list_certificates(request):
    cert_list = Certificate.objects.all()
    return render(request, 'events/certificates.html', {'cert_list': cert_list})


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


def delete_consultant(request, consultant_id):
    consultant = Consultant.objects.get(pk=consultant_id)
    consultant.delete()
    return redirect('consultants')


def update_consultant(request, consultant_id):
    consultant = Consultant.objects.get(pk=consultant_id)
    form = ConsultantForm(request.POST or None, instance=consultant)
    if form.is_valid():
        form.save()
        return redirect('list_consultants')
    return render(request, 'events/update_consultant.html', {'consultant': consultant, 'form': form})


def show_consultant(request, consultant_id):
    consultant = Consultant.objects.get(pk=consultant_id)
    return render(request, 'events/show_consultant.html', {'consultant': consultant})


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


def index(request):
    list_events = Event.objects.all()
    context = {
        "events": list_events,
    }
    return render(request, 'events/index.html', context)


def list_events(request):
    list_events = Event.objects.all()
    out = []
    for event in list_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events.html', {'event_list': event_list})


def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'events/show_event.html', {'event': event})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('all_events')
    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('all_events')


def add_events(request):
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


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Event(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
