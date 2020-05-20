from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE,primary_key=True)
    familiya=models.CharField(max_length=50,blank=True,default='')
    imya=models.CharField(max_length=50,blank=True,default='')
    otchestvo=models.CharField(max_length=50,blank=True,default='')
    #svyaz
    phone=models.CharField(max_length=50,blank=True,default='')
    email=models.EmailField(max_length=50,blank=True,default='')
    #passport
    seriya = models.IntegerField(default=0)
    nomer = models.IntegerField(default=0)
    POL=(
        ('1', 'Мужской'),
        ('2', 'Женский'),
        )
    pol= models.CharField(max_length=20,choices=POL,default='')
    ORGAN=(
        ('1', 'organ1'),
        ('2', 'organ2'),
        )
    organ= models.CharField(max_length=20,choices=ORGAN,default='')
    #spec
    SPEC=(
        ('БИТ10,1,1,', 'ПД'),
        ('фпсоиб', 'фпсоиб'),
        )
    FAC = (
        ('фпсоиб', 'фпсоиб'),
        ('БИТ10,1,1,', 'ПД'),
    )
    special=models.CharField(max_length=50,choices=SPEC,default='')
    facult=models.CharField(max_length=50,choices=FAC,default='')

    #EGE
    russ = models.IntegerField(default=0)
    mat = models.IntegerField(default=0)
    obsh = models.IntegerField(default=0)
    biol = models.IntegerField(default=0)
    zayavl = models.FileField(upload_to='files',default=None)
    #право доступа, 1- обычный пользователь 2-привелигированный
    role = models.IntegerField(default=1)
    #1-превая форма 2 доки 3 заявление
    dopinfo=models.BooleanField(default=False,blank=True)
    def __str__(self):
        return self.user.username
    def getData(self):
        return ([
        str(self.familiya),
        str(self.imya),
        str(self.otchestvo),
        str(self.seriya),
        str(self.nomer),
        str(self.organ),
        str(self.special),
        str(self.facult),
        str(self.russ),
        str(self.obsh),
        str(self.mat),
        str(self.biol),
        str(self.phone),
        str(self.email),
        ])
    def checkAnket(self):
        if (''==self.familiya
            or ''==self.imya
            or ''==self.otchestvo
            or ''==self.phone
            or ''==self.email
            or 0==self.seriya
            or 0==self.nomer
            or ''==self.pol
            or ''==self.organ
            or ''==self.special
            or ''==self.facult
            or 0==self.russ):
            # or 0==self.mat
            # or 0==self.obsh
            # or 0==self.biol

            return False
        else:
            return True
    def checkZayavl(self):
        if not self.zayavl:
            return False
        else:
            return True





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
