# Generated by Django 3.0.1 on 2020-04-12 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0030_user_meta_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_meta',
            name='last_login',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
