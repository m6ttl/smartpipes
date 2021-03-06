# Generated by Django 2.0.1 on 2018-08-22 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_auto_20180812_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citydict',
            options={'verbose_name': '服务机构', 'verbose_name_plural': '服务机构'},
        ),
        migrations.AlterField(
            model_name='citydict',
            name='name',
            field=models.CharField(max_length=20, verbose_name='服务机构'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='address',
            field=models.CharField(max_length=150, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(max_length=100, verbose_name='类型试题'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='服务机构'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(max_length=10, verbose_name='类型标签'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='work_company',
            field=models.CharField(max_length=50, verbose_name='专长'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='work_position',
            field=models.CharField(max_length=50, verbose_name='江湖称号'),
        ),
    ]
