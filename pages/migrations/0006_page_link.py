# Generated by Django 2.1.9 on 2019-06-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20190611_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='link',
            field=models.CharField(default='', max_length=50),
        ),
    ]
