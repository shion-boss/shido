# Generated by Django 3.0.1 on 2020-03-28 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0014_channel_model_channel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_meta',
            name='photo',
            field=models.ImageField(default='media/defo.jpg', upload_to='media/media/'),
        ),
    ]
