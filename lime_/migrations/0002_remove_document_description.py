# Generated by Django 2.1.3 on 2018-12-01 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lime_', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]
