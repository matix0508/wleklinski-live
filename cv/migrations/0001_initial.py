# Generated by Django 3.0.5 on 2020-07-06 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=20)),
                ('field', models.CharField(max_length=20)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=100)),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TechSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech1', to='cv.Technology')),
                ('tech2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech2', to='cv.Technology')),
                ('tech3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech3', to='cv.Technology')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('job', models.CharField(max_length=30)),
                ('workplace', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('technologies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.TechSet')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('time', models.DateField(blank=True, null=True)),
                ('technologies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.TechSet')),
            ],
        ),
    ]
