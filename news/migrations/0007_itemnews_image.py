# Generated by Django 2.1.9 on 2019-06-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_itemnews_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemnews',
            name='image',
            field=models.ImageField(blank=True, upload_to='news/'),
        ),
    ]
