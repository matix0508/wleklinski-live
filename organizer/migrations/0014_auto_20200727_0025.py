# Generated by Django 3.0.5 on 2020-07-26 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0013_auto_20200602_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gogame',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 27)),
        ),
    ]
