# Generated by Django 5.0 on 2024-01-01 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_consultant_cons_id_remove_event_instructor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultant',
            name='cons_ID',
        ),
    ]