# Generated by Django 4.0.6 on 2022-07-18 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='data',
            new_name='date',
        ),
    ]
