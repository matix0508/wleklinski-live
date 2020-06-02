# Generated by Django 3.0.5 on 2020-06-01 23:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizer', '0012_auto_20200524_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='gogame',
            name='date',
            field=models.DateField(default=datetime.date(2020, 6, 2)),
        ),
        migrations.CreateModel(
            name='LearningGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('goal', models.FloatField(null=True)),
                ('due', models.DateField(blank=True, null=True)),
                ('done', models.FloatField(blank=True, default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Subject')),
            ],
        ),
    ]
