# Generated by Django 3.0.1 on 2020-03-31 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0018_user_meta_qrcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='afirieito_model',
            old_name='username',
            new_name='introducer',
        ),
    ]
