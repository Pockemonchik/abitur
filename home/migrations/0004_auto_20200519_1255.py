# Generated by Django 3.0.6 on 2020-05-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile_dostizhfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dostizh',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dostizhFile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='osobpravo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='osobpravoFile',
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facult',
            field=models.CharField(choices=[('фпсоиб', 'фпсоиб'), ('БИТ10,1,1,', 'ПД')], default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='familiya',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='imya',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='otchestvo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='special',
            field=models.CharField(choices=[('БИТ10,1,1,', 'ПД'), ('фпсоиб', 'фпсоиб')], default=' ', max_length=50),
        ),
        migrations.CreateModel(
            name='OsobDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('doc', models.FileField(default='', upload_to='files')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='DostizhDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('doc', models.FileField(default='', upload_to='files')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
    ]
