# Generated by Django 4.0.1 on 2022-08-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_alter_members_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='type',
            field=models.CharField(max_length=4, verbose_name='類型'),
        ),
        migrations.AlterField(
            model_name='members',
            name='thumb',
            field=models.IntegerField(default=0, null=True, verbose_name='按讚次數'),
        ),
    ]