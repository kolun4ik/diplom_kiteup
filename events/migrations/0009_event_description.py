# Generated by Django 2.1.9 on 2019-06-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
