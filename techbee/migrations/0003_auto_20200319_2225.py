# Generated by Django 3.0.1 on 2020-03-19 13:25

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0002_user_meta_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_meta',
            name='name',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=20),
        ),
    ]