# Generated by Django 2.1.9 on 2019-07-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190712_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date_creation',
            new_name='created',
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
