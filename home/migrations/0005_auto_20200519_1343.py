# Generated by Django 3.0.6 on 2020-05-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200519_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='dostizhdocument',
            name='type',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='osobdocument',
            name='type',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='dostizhdocument',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='osobdocument',
            name='name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
