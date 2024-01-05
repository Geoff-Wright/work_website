from django.forms import ModelForm
from .models import *
from django import forms


class ConsultantForm(ModelForm):
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


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date_from', 'event_date_to', 'venue', 'contact', 'instructor')
        labels = {
            'name': '',
            'event_date_from': '',
            'event_date_to': '',
            'venue': 'Venue',
            'contact': '',
            'instructor': 'Instructor',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Event"}),
            'event_date_from': forms.DateInput(
                format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'event_date_to': forms.DateInput(
                format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': "Venue"}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Contact"}),
            'instructor': forms.Select(attrs={'class': 'form-select', 'placeholder': "Instructor"}),
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
