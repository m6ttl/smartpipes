# Generated by Django 2.0.1 on 2018-10-10 15:59

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_coursecomments_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomments',
            name='ctitle',
            field=models.CharField(default='交流', max_length=30, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='comments',
            field=mdeditor.fields.MDTextField(verbose_name='交流'),
        ),
        migrations.AlterField(
            model_name='coursecomments',
            name='kind',
            field=models.CharField(choices=[('pl', '交流'), ('qt', '其他'), ('zx', '咨询'), ('jy', '建议')], default='pl', max_length=2, verbose_name='类型'),
        ),
    ]
