from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    room = models.CharField('Room', max_length=25)
    zip_code = models.CharField('Zip Code', max_length=15, null=True)
    phone = models.CharField('Contact Phone', max_length=25)
    web = models.URLField('Website Address', null=True)
    email_address = models.EmailField('Email Address', null=True)
    # 'name' 'address 'room' 'zip_code' 'phone' 'web' 'email_address'

    def __str__(self):
        return self.name


class Consultant(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('Email Address')
    phone = models.CharField('Contact Phone', max_length=25)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date_from = models.DateTimeField('Event_Date_From')
    event_date_to = models.DateTimeField('Event Date To')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    contact = models.CharField('Contact', max_length=60)
    instructor = models.ManyToManyField(Consultant, blank=True)
    # 'name', 'event_date_from', 'event_date_to', 'venue', 'contact', 'instructor'

    def __str__(self):
        return self.name
