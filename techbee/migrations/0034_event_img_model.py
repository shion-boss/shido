# Generated by Django 3.0.1 on 2020-04-14 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techbee', '0033_auto_20200413_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_img_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techbee.event_model')),
            ],
        ),
    ]
