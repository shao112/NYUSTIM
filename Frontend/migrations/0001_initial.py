# Generated by Django 4.0.1 on 2022-07-25 15:46

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='稱謂')),
                ('department', models.TextField(verbose_name='科系')),
                ('date', models.TextField(verbose_name='日期')),
                ('time', models.TextField(verbose_name='時間')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='電子信箱')),
                ('msg', models.TextField(verbose_name='留言')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='建立日期')),
                ('update_date', models.DateField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '預約友誼賽',
                'verbose_name_plural': '預約友誼賽',
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='標題')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='編輯器內文')),
                ('image', models.ImageField(upload_to='competition', verbose_name='封面圖')),
                ('editor', models.CharField(max_length=10, verbose_name='編輯者')),
                ('type', models.CharField(choices=[('1', '聯賽'), ('2', '系際盃'), ('3', '校外'), ('4', '新生盃'), ('5', '小資杯')], max_length=1)),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='建立日期')),
                ('update_date', models.DateField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '賽事報導',
                'verbose_name_plural': '賽事報導',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, verbose_name='姓名')),
                ('description', models.TextField(verbose_name='成員介紹')),
                ('image', models.ImageField(upload_to='members', verbose_name='照片')),
                ('grade', models.CharField(max_length=3, verbose_name='級次')),
                ('position', models.CharField(choices=[('1', '大砲'), ('2', '舉球'), ('3', '自由'), ('4', '副攻'), ('5', '欄中'), ('6', '輔舉'), ('7', '耍寶')], max_length=1)),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='建立日期')),
                ('update_date', models.DateField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '歷屆成員',
                'verbose_name_plural': '歷屆成員',
                'ordering': ['-id'],
            },
        ),
    ]
