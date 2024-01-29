# Generated by Django 5.0 on 2024-01-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='number_of_days',
            new_name='course_duration',

        ),

        migrations.AddField(
            model_name='course',
            name='course_version',
            field=models.IntegerField(null=True, verbose_name='Course Version'),
        ),
        migrations.AlterField(
            model_name='course',
            name='certification',
            field=models.CharField(max_length=100, null=True, verbose_name='Certification'),
        ),
    ]