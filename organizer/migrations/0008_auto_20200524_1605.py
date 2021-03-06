# Generated by Django 3.0.5 on 2020-05-24 14:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizer', '0007_auto_20200512_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('total_cost', models.FloatField(null=True)),
                ('cost_per_person', models.FloatField(null=True)),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('person2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2', to=settings.AUTH_USER_MODEL)),
                ('person3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3', to=settings.AUTH_USER_MODEL)),
                ('person4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p4', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='gogame',
            name='date',
            field=models.DateField(default=datetime.date(2020, 5, 24)),
        ),
        migrations.CreateModel(
            name='TripCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
                ('split', models.BooleanField(default=False)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Trip')),
            ],
        ),
    ]
