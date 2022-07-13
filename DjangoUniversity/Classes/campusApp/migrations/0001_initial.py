# Generated by Django 4.0.6 on 2022-07-13 20:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CampusName', models.CharField(blank=True, default='', max_length=60)),
                ('State', models.CharField(blank=True, default='', max_length=60)),
                ('CampusID', models.IntegerField(blank=True, default='')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]