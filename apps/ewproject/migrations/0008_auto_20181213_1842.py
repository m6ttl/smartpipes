# Generated by Django 2.0.1 on 2018-12-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewproject', '0007_auto_20181213_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ewproject',
            name='area_rank',
            field=models.CharField(blank=True, default='市', max_length=20, null=True, verbose_name='级别'),
        ),
    ]
