# Generated by Django 5.0 on 2024-01-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_remove_certificate_cert_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='cert_attained',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='cert_expires',
        ),
        migrations.AddField(
            model_name='certificate',
            name='cert_type',
            field=models.CharField(max_length=100, null=True, verbose_name='Cert Title'),
        ),
    ]
