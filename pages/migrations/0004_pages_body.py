# Generated by Django 2.1.9 on 2019-06-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190610_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
