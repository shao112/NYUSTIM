from email import message
from django.db import models
from django.utils import timezone
# django-ckeditor
from ckeditor_uploader.fields import RichTextUploadingField

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
        ('7', '打雜'),
    )
    name = models.CharField(max_length=4, verbose_name="姓名")
    description = models.TextField(verbose_name='成員介紹')
    image = models.ImageField(upload_to="members", verbose_name='照片')
    grade = models.CharField(max_length=3, verbose_name="級次")
    position = models.CharField(max_length=1, choices=Position_type)
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "歷屆成員"   # 單數
        verbose_name_plural = verbose_name   #複數
        ordering = ['-id']
        # order_with_respect_to = 'id'

# 賽事報導

class Competition(models.Model):
    Competition_type = (
        ('1', '聯賽'),
        ('2', '系際盃'),
        ('3', '校外'),
        ('4', '新生盃'),
        ('5', '小資杯'),
    )
    title = models.CharField(max_length=30, verbose_name="標題")
    content = RichTextUploadingField(verbose_name='編輯器內文' ,blank=True, null=True)
    image = models.ImageField(upload_to="competition", verbose_name='封面圖')
    editor = models.CharField(max_length=10, verbose_name="編輯者")
    type = models.CharField(max_length=1, choices=Competition_type)
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "賽事報導"   # 單數
        verbose_name_plural = verbose_name   #複數

# 活動公告

# 預約友誼賽

class Appointment(models.Model):
    Position_type = (
        ('1', '大砲'),
        ('2', '舉球'),
        ('3', '自由'),
        ('4', '副攻'),
        ('5', '欄中'),
        ('6', '輔舉'),
        ('7', '打雜'),
    )
    name = models.CharField(max_length=20, verbose_name="稱謂")
    Department = models.TextField(verbose_name='科系')
    date = models.TextField(verbose_name="日期")
    time = models.TextField(verbose_name="時間")
    email = models.EmailField(max_length=30,unique=True, verbose_name='電子信箱')
    msg = models.TextField(verbose_name="留言")
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "預約友誼賽"   # 單數
        verbose_name_plural = verbose_name   #複數