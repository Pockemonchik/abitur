# Generated by Django 3.0.6 on 2020-05-19 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('familiya', models.CharField(blank=True, max_length=1000)),
                ('imya', models.CharField(blank=True, max_length=1000)),
                ('otchestvo', models.CharField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('seriya', models.IntegerField(default=1)),
                ('nomer', models.IntegerField(default=1)),
                ('pol', models.CharField(choices=[('1', 'Мужской'), ('2', 'Женский')], default=' ', max_length=20)),
                ('organ', models.CharField(choices=[('1', 'organ1'), ('2', 'organ2')], default=' ', max_length=20)),
                ('special', models.CharField(choices=[('БИТ10,1,1,', 'ПД'), ('фпсоиб', 'фпсоиб')], default=' ', max_length=20)),
                ('facult', models.CharField(choices=[('фпсоиб', 'фпсоиб'), ('БИТ10,1,1,', 'ПД')], default=' ', max_length=20)),
                ('russ', models.IntegerField(default=0)),
                ('mat', models.IntegerField(default=0)),
                ('obsh', models.IntegerField(default=0)),
                ('biol', models.IntegerField(default=0)),
                ('dostizh', models.CharField(choices=[('нет', 'нет'), ('otl', 'otl'), ('sport,', 'sport')], default='нет', max_length=20)),
                ('dostizhFile', models.FileField(default='', upload_to='files')),
                ('osobpravo', models.CharField(choices=[('нет', 'нет'), ('otl', 'otl'), ('sport,', 'sport')], default='нет', max_length=20)),
                ('osobpravoFile', models.FileField(default='', upload_to='files')),
                ('zayavl', models.FileField(default='', upload_to='files')),
                ('role', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
