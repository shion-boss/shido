# Generated by Django 3.0.1 on 2020-04-22 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0041_auto_20200421_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts_model',
            name='file_name',
            field=models.CharField(max_length=30),
        ),
    ]
