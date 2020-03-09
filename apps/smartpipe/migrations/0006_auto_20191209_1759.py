# Generated by Django 2.0.1 on 2019-12-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartpipe', '0005_auto_20191209_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartpipe',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='pipedetail',
            name='pipe_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartpipe.smartpipe', verbose_name='管件编号'),
        ),
    ]
