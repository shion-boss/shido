# Generated by Django 3.0.1 on 2020-03-23 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0012_like_model_like_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories_model',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
