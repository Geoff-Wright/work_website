# Generated by Django 5.0 on 2024-01-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_remove_course_course_duration_course_number_of_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='number_of_days',
        ),
        migrations.AddField(
            model_name='course',
            name='course_duration',
            field=models.IntegerField(null=True, verbose_name='Duration'),
        ),
    ]
