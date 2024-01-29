# Generated by Django 5.0 on 2024-01-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_remove_event_event_date_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_duration',
        ),
        migrations.AddField(
            model_name='course',
            name='number_of_days',
            field=models.IntegerField(null=True, verbose_name='number_of_days (Days)'),
        ),
    ]