# Generated by Django 2.0.1 on 2018-12-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewproject', '0008_auto_20181213_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='ewproject',
            name='p_status',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='状态'),
        ),
    ]
