# Generated by Django 3.0.1 on 2020-04-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0040_event_model_event_dis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_model',
            name='event_dis',
            field=models.TextField(blank=True, max_length=140, null=True),
        ),
    ]
