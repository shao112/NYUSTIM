from email import message
from django.db import models
from django.utils import timezone
# django-ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from itertools import chain

# Create your models here.

# 歷屆成員 / 成員介紹

class Members(models.Model):
    Position_type = (
        ('1', '大砲'),
        ('2', '舉球'),
        ('3', '自由'),
        ('4', '副攻'),
        ('5', '欄中'),
        ('6', '輔舉'),
        ('7', '耍寶'),
    )
    name = models.CharField(max_length=4, verbose_name="姓名")
    description = models.TextField(verbose_name='成員介紹')
    image = models.ImageField(upload_to="membersImage", verbose_name='照片')
    grade = models.CharField(max_length=3, verbose_name="級次")
    thumb = models.IntegerField(default=0, verbose_name="按讚次數", null=True)
    position = models.CharField(max_length=1, choices=Position_type, verbose_name="位置")
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "歷屆成員"   # 單數
        verbose_name_plural = verbose_name   #複數
        ordering = ['-id']
        # order_with_respect_to = 'id'

    def to_dict(self):
        opts = self._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            print("_____________")
            print(f.name)
            if f.name == 'image':
                data[f.name] = f.value_from_object(self).url
                print(f.value_from_object(self).url)
            else:
                data[f.name] = f.value_from_object(self)
        return data

# 賽事報導

class Competition(models.Model):
    Competition_type = (
        ('1', '聯賽'),
        ('2', '系際盃'),
        ('3', '校外'),
        ('4', '新生盃'),
        ('5', '友誼賽'),
        ('6', '小資杯'),
    )
    title = models.CharField(max_length=30, verbose_name="標題")
    content = RichTextUploadingField(verbose_name='編輯器內文' ,blank=True, null=True)
    image = models.ImageField(upload_to="competitionImage", verbose_name='封面圖')
    editor = models.CharField(max_length=10, verbose_name="編輯者")
    type = models.CharField(max_length=1, choices=Competition_type)
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "賽事報導"   # 單數
        verbose_name_plural = verbose_name   #複數

    def to_dict(self):
        opts = self._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            print("_____________")
            print(f.name)
            if f.name == 'image':
                data[f.name] = f.value_from_object(self).url
                print(f.value_from_object(self).url)
            else:
                data[f.name] = f.value_from_object(self)
        return data

# 活動公告
class Events(models.Model):
    
    type = models.CharField(max_length=4, verbose_name="類型")
    content = models.TextField(verbose_name='內容')
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "活動公告"   # 單數
        verbose_name_plural = verbose_name   #複數

    def to_dict(self):
        opts = self._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            print("_____________")
            print(f.name)
            if f.name == 'image':
                data[f.name] = f.value_from_object(self).url
                print(f.value_from_object(self).url)
            else:
                data[f.name] = f.value_from_object(self)
        return data

# 預約友誼賽

class Appointment(models.Model):

    name = models.CharField(max_length=20, verbose_name="稱謂")
    department = models.TextField(verbose_name='科系')
    date = models.TextField(verbose_name="日期")
    time = models.TextField(verbose_name="時間")
    email = models.EmailField(max_length=30,unique=True, verbose_name='電子信箱')
    msg = models.TextField(verbose_name="留言")
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "預約友誼賽"   # 單數
        verbose_name_plural = verbose_name   #複數
    
    def to_dict(self):
        opts = self._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            print("_____________")
            print(f.name)
            if f.name == 'image':
                data[f.name] = f.value_from_object(self).url
                print(f.value_from_object(self).url)
            else:
                data[f.name] = f.value_from_object(self)
        return data