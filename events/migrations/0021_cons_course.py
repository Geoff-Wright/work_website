# Generated by Django 5.0 on 2024-02-12 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_remove_certificate_cert_attained_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cons_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.IntegerField(default=0, verbose_name='choice')),
                ('consultant', models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='events.consultant')),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='events.course')),
            ],
        ),
    ]