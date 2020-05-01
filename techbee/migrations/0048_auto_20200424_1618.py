# Generated by Django 3.0.1 on 2020-04-24 16:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0047_user_meta_give_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_meta',
            name='give_like',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]