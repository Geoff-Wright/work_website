from django.forms import ModelForm
from .models import *
from django import forms

CHOICES = {"1": "Taught", "2": "Could Do", "3": "Like to do"}


class ConsCourseForm(ModelForm):
    class Meta:
        model = Cons_Course
        fields = ('consultant', 'course', 'choice')
        labels = {
            'consultant': '',
            'course': '',
            'choice': '',
        }
        widgets = {
            'consultant': forms.Select(
                attrs={'class': 'form-select', 'placeholder': "Consultant"}),
            'course': forms.Select(
                attrs={'class': 'form-select', 'placeholder': "Course"}),
            'choice': forms.RadioSelect(choices=CHOICES),
        }


class ConsultantForm(ModelForm):
    Consultant = models.CharField(max_length=200, default="")

    class Meta:
        model = Consultant
        fields = ('first_name', 'last_name', 'email', 'phone')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email Address"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Phone"}),
        }

    def __unicode__(self):
        return self.Consultant


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'status', 'start', 'end', 'venue', 'instructor')
        labels = {
            'name': '',
            'status': '',
            'start': 'Event Start',
            'end': 'Event End',
            'venue': '',
            'instructor': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Event"}),
            'status': forms.Select(
                attrs={'class': 'form-select', 'placeholder': "Status"}),
            'start': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'}),
            'venue': forms.Select(
                attrs={'class': 'form-select', 'placeholder': "Venue"}),
            'instructor': forms.Select(
                attrs={'class': 'form-select', 'placeholder': "Instructor"}),
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'room', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'room': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Venue"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Address"}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Room"}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Zip-Code"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Phone"}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Web Site"}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
        }
