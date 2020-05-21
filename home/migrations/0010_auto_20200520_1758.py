# Generated by Django 3.0.6 on 2020-05-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200520_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facult',
            field=models.CharField(choices=[('фпсоиб', 'фпсоиб'), ('БИТ10,1,1,', 'ПД')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='familiya',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='imya',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organ',
            field=models.CharField(choices=[('1', 'organ1'), ('2', 'organ2')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='otchestvo',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pol',
            field=models.CharField(choices=[('1', 'Мужской'), ('2', 'Женский')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='special',
            field=models.CharField(choices=[('БИТ10,1,1,', 'ПД'), ('фпсоиб', 'фпсоиб')], default='', max_length=50),
        ),
    ]