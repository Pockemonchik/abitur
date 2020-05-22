from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE,primary_key=True)
    familiya=models.CharField(max_length=100,blank=True,default='')
    imya=models.CharField(max_length=100,blank=True,default='')
    otchestvo=models.CharField(max_length=100,blank=True,default='')
    #svyaz
    phone=models.CharField(max_length=100,blank=True,default='')
    email=models.EmailField(max_length=100,blank=True,default='')
    #passport
    seriya = models.IntegerField(default=0)
    nomer = models.IntegerField(default=0)
    POL=(
        ('1', 'Мужской'),
        ('2', 'Женский'),
        )
    pol= models.CharField(max_length=100,choices=POL,default='')
    ORGAN=(
        ('БСТМ МВД России', 'БСТМ МВД России'),

        ('ДГСК МВД России', 'ДГСК МВД России'),

        ('ГУВМ МВД России', 'ГУВМ МВД России'),

        ('ОПБ МВД России', 'ОПБ МВД России'),

        ('ФЭД МВД России','ФЭД МВД России'),

        ('ЦСН БДД МВД России','ЦСН БДД МВД России'),

        ('МВД по Республике Бурятия', 'МВД по Республике Бурятия'),

        ('МВД по Республике Дагестан', 'МВД по Республике Дагестан'),

        ('МВД по Республике Ингушетия', 'МВД по Республике Ингушетия'),

        ('МВД по Республике Калмыкия', 'МВД по Республике Калмыкия'),

        ('МВД по Республике Коми', 'МВД по Республике Коми'),

        ('МВД по Республике Марий Эл', 'МВД по Республике Марий Эл'),

        ('МВД по Республике Мордовия', 'МВД по Республике Мордовия'),

        ('МВД по Республике Саха (Якутия)', 'МВД по Республике Саха (Якутия)'),

        ('МВД по Удмуртской Республике', 'МВД по Удмуртской Республике'),

        ('ГУ МВД России по г. Москве', 'ГУ МВД России по г. Москве'),

        ('ГУ МВД России по Московской области', 'ГУ МВД России по Московской области'),

        ('ГУ МВД России по Ставропольскому краю', 'ГУ МВД России по Ставропольскому краю'),

        ('ГУ МВД России по Воронежской области', 'ГУ МВД России по Воронежской области'),

        ('ГУ МВД России по Иркутской области', 'ГУ МВД России по Иркутской области'),

        ('ГУ МВД России по Ростовской области', 'ГУ МВД России по Ростовской области'),

        ('УМВД России по г. Севастополю', 'УМВД России по г. Севастополю'),

        ('УМВД России по Забайкальскому краю', 'УМВД России по Забайкальскому краю'),

        ('УМВД России по Астраханской области', 'УМВД России по Астраханской области'),

        ('УМВД России по Белгородской области', 'УМВД России по Белгородской области'),

        ('УМВД России по Брянской области', 'УМВД России по Брянской области'),

        ('УМВД России по Владимирской области', 'УМВД России по Владимирской области'),

        ('УМВД России по Ивановской области', 'УМВД России по Ивановской области'),

        ('УМВД России по Калужской области', 'УМВД России по Калужской области'),

        ('УМВД России по Кировской области', 'УМВД России по Кировской области'),

        ('УМВД России по Костромской области', 'УМВД России по Костромской области'),

        ('УМВД России по Курской области', 'УМВД России по Курской области'),

        ('УМВД России по Липецкой области', 'УМВД России по Липецкой области'),

        ('УМВД России по Орловской области', 'УМВД России по Орловской области'),

        ('УМВД России по Пензенской области', 'УМВД России по Пензенской области'),

        ('УМВД России по Рязанской области', 'УМВД России по Рязанской области'),

        ('УМВД России по Смоленской области', 'УМВД России по Смоленской области'),

        ('УМВД России по Тамбовской области', 'УМВД России по Тамбовской области'),

        ('УМВД России по Тверской области', 'УМВД России по Тверской области'),

        ('УМВД России по Тульской области', 'УМВД России по Тульской области'),

        ('УМВД России по Ярославской области', 'УМВД России по Ярославской области'),

        ('УМВД России по Еврейской автономной области', 'УМВД России по Еврейской автономной области'),

        ('УТ МВД России по ЦФО', 'УТ МВД России по ЦФО'),

        ('Московский университет МВД России имени В.Я. Кикотя', 'Московский университет МВД России имени В.Я. Кикотя'),

        ('Всероссийский институт повышения квалификации сотрудников МВД России', 'Всероссийский институт повышения квалификации сотрудников МВД России'),

        ('Читинское суворовское военное училище МВД России', 'Читинское суворовское военное училище МВД России'),
        )
    organ= models.CharField(max_length=100,choices=ORGAN,default='',blank=True)
    #spec
    SPEC=(
        ('ПД', 'ПД'),
        ('фпсоиб', 'фпсоиб'),
        )
    FAC = (
        ('фпсоиб', 'фпсоиб'),
        ('ПД', 'ПД'),
    )
    # special=models.CharField(max_length=100,choices=SPEC,default='',blank=True)
    # facult=models.CharField(max_length=100,choices=FAC,default='',blank=True)
    special=models.CharField(max_length=100,choices=FAC,default='',blank=True)
    facult=models.CharField(max_length=100,default='',blank=True)

    #EGE
    russ = models.IntegerField(default=0)
    mat = models.IntegerField(default=0)
    obsh = models.IntegerField(default=0)
    biol = models.IntegerField(default=0)
    zayavl = models.FileField(upload_to='files',default=None,blank=True)
    #право доступа, 1- обычный пользователь 2-привелигированный
    role = models.IntegerField(default=1)
    #1-превая форма 2 доки 3 заявление
    dopinfo=models.BooleanField(default=False,blank=True)
    dopusk=models.BooleanField(default=False,blank=True)
    balli = models.IntegerField(default=0,blank=True)
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
    type=models.CharField(max_length=1000,blank=True)
    name=models.CharField(max_length=1000,blank=True)
    doc = models.FileField(upload_to='files',default='',blank=True)
    def __str__(self):
            return self.profile.familiya+"особ право"

class DostizhDocument(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    type=models.CharField(max_length=1000,blank=True)
    name=models.CharField(max_length=1000,blank=True)
    doc = models.FileField(upload_to='files',default='',blank=True)
    def __str__(self):
            return self.profile.familiya+"достижения"
