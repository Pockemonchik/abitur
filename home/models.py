from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete="cascade",primary_key=True)
    familiya=models.CharField(max_length=1000,blank=True)
    imya=models.CharField(max_length=1000,blank=True)
    otchestvo=models.CharField(max_length=250,blank=True)
    #svyaz
    phone=models.CharField(max_length=250,blank=True)
    email=models.EmailField(max_length=250,blank=True)
    #passport
    seriya = models.IntegerField(default=1)
    nomer = models.IntegerField(default=1)
    POL=(
        ('1', 'Мужской'),
        ('2', 'Женский'),
        )
    pol= models.CharField(max_length=20,choices=POL,default=" ")
    ORGAN=(
        ('1', 'organ1'),
        ('2', 'organ2'),
        )
    organ= models.CharField(max_length=20,choices=ORGAN,default=" ")
    #spec
    SPEC=(
        ('БИТ10,1,1,', 'ПД'),
        ('фпсоиб', 'фпсоиб'),
        )
    FAC = (
        ('фпсоиб', 'фпсоиб'),
        ('БИТ10,1,1,', 'ПД'),
    )
    special=models.CharField(max_length=20,choices=SPEC,default=" ")
    facult=models.CharField(max_length=20,choices=FAC,default=" ")

    #EGE
    russ = models.IntegerField(default=0)
    mat = models.IntegerField(default=0)
    obsh = models.IntegerField(default=0)
    biol = models.IntegerField(default=0)
    #individ dostizh
    DOST=(
        ('нет', 'нет'),
        ('otl', 'otl'),
        ('sport,', 'sport'))
    OSOB=(
        ('нет', 'нет'),
        ('otl', 'otl'),
        ('sport,', 'sport'))
    dostizh = models.CharField(max_length=20,choices=DOST,default="нет")
    dostiszhFile = models.FileField(upload_to='files',default='settings.MEDIA_ROOT/example.docx')
    osobpravo = models.CharField(max_length=20,choices=OSOB,default="нет")
    osobpravoFile = models.FileField(upload_to='files',default='settings.MEDIA_ROOT/example.docx')
    zayavl = models.FileField(upload_to='files',default='settings.MEDIA_ROOT/example.docx')
    #право доступа, 1- обычный пользователь 2-привелигированный
    role = models.IntegerField(default=1)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
