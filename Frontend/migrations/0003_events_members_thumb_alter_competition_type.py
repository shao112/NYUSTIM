# Generated by Django 4.0.1 on 2022-07-26 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_alter_competition_image_alter_members_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='類型')),
                ('content', models.TextField(verbose_name='內容')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='建立日期')),
                ('update_date', models.DateField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '活動公告',
                'verbose_name_plural': '活動公告',
            },
        ),
        migrations.AddField(
            model_name='members',
            name='thumb',
            field=models.IntegerField(null=True, verbose_name='按讚次數'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='type',
            field=models.CharField(choices=[('1', '聯賽'), ('2', '系際盃'), ('3', '校外'), ('4', '新生盃'), ('5', '友誼賽'), ('6', '小資杯')], max_length=1),
        ),
    ]
