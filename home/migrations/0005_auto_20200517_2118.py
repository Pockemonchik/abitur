# Generated by Django 2.2.3 on 2020-05-17 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile_familiya'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dostiszh',
            new_name='dostizh',
        ),
    ]
