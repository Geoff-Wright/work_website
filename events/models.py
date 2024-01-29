from django.db import models
from django_better_choices import Choices


class EventStatus(Choices):
    CREATED = 'Created'
    PENDING = Choices.Value('Pending', help_text='This set status to pending')
    SOFTBOOKED = Choices.Value('Soft Booked', help_text='This set status to pending')
    HARDBOOKED = Choices.Value('Hard Booked', help_text='This set status to pending')
    ON_HOLD = Choices.Value('On Hold', value='custom_on_hold')
    VALID = Choices.Subset('CREATED', 'ON_HOLD')

    class INTERNAL_STATUS(Choices):
        REVIEW = 'On Review'

    @classmethod
    def get_help_text(cls):
        return tuple(
            value.help_text
            for value in cls.values()
            if hasattr(value, 'help_text')
        )


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
    # 'first_name' 'last_name' 'email' 'phone'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Course(models.Model):
    course_number = models.CharField('Course Identifier', max_length=25)
    course_version = models.IntegerField('Course Version', null=True)
    course_title = models.CharField('Course Title', max_length=200)
    course_duration = models.IntegerField('Duration', null=True)
    certification = models.CharField('Certification', max_length=100, null=True)

    def __str__(self):
        return self.course_number


class Certificate(models.Model):
    certification = models.CharField('Certification', max_length=25, null=True)
    cert_title = models.CharField('Cert Title', max_length=250, null=True)
    cert_type = models.CharField('Cert Title', max_length=100, null=True)

    def __str__(self):
        return self.certification


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    status = models.CharField(choices=EventStatus, default=EventStatus.PENDING, max_length=25)
    start = models.DateTimeField('start', default="2024-01-01 00:00:00")
    end = models.DateTimeField('end', default="2024-01-01 00:00:00")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.PROTECT)
    instructor = models.ForeignKey(Consultant, blank=True, null=True, on_delete=models.PROTECT)
    # 'name', 'start', 'end', 'venue', 'contact', 'instructor'

    def __str__(self):
        return self.name
