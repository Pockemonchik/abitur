# Generated by Django 3.0.6 on 2020-05-19 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dostizhFile',
        ),
    ]
