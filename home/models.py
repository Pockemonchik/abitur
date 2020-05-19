from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE,primary_key=True)
    familiya=models.CharField(max_length=50,blank=True)
    imya=models.CharField(max_length=50,blank=True)
    otchestvo=models.CharField(max_length=50,blank=True)
    #svyaz
    phone=models.CharField(max_length=50,blank=True)
    email=models.EmailField(max_length=50,blank=True)
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
    special=models.CharField(max_length=50,choices=SPEC,default=" ")
    facult=models.CharField(max_length=50,choices=FAC,default=" ")

    #EGE
    russ = models.IntegerField(default=0)
    mat = models.IntegerField(default=0)
    obsh = models.IntegerField(default=0)
    biol = models.IntegerField(default=0)
    #individ dostizh
    # DOST=(
    #     ('нет', 'нет'),
    #     ('otl', 'otl'),
    #     ('sport,', 'sport'))
    # OSOB=(
    #     ('нет', 'нет'),
    #     ('otl', 'otl'),
    #     ('sport,', 'sport'))
    # dostizh = models.CharField(max_length=100,choices=DOST,default="нет")
    # osobpravo = models.CharField(max_length=100,choices=OSOB,default="нет")
    zayavl = models.FileField(upload_to='files',default='')
    #право доступа, 1- обычный пользователь 2-привелигированный
    role = models.IntegerField(default=1)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

class OsobDocument(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    type=models.CharField(max_length=500,blank=True)
    name=models.CharField(max_length=500,blank=True)
    doc = models.FileField(upload_to='files',default='',blank=True)
    def __str__(self):
            return self.profile.familiya+"особ право"

class DostizhDocument(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    type=models.CharField(max_length=500,blank=True)
    name=models.CharField(max_length=500,blank=True)
    doc = models.FileField(upload_to='files',default='',blank=True)
    def __str__(self):
            return self.profile.familiya+"достижения"
