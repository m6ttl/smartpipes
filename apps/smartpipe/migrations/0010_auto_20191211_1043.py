# Generated by Django 2.0.1 on 2019-12-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpipe', '0009_auto_20191211_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='latitude',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='纬度'),
        ),
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='纬度'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='latitude',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='纬度'),
        ),
    ]
