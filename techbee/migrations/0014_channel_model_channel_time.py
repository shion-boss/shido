# Generated by Django 3.0.1 on 2020-03-24 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0013_categories_model_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel_model',
            name='channel_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]