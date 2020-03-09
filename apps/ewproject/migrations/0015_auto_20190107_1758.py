# Generated by Django 2.0.1 on 2019-01-07 17:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ewproject', '0014_projectchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '报告附件',
                'verbose_name_plural': '报告附件',
            },
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='阅读时间')),
            ],
            options={
                'verbose_name': '报告阅读用用户',
                'verbose_name_plural': '报告阅读用用户',
            },
        ),
        migrations.RemoveField(
            model_name='ewreport',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='ewreport',
            name='title',
        ),
        migrations.AddField(
            model_name='ewreport',
            name='download',
            field=models.FileField(default=1, upload_to='course/resource/%Y/%m', verbose_name='HTML报告'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ewreport',
            name='build_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='ewreport',
            name='typen',
            field=models.CharField(blank=True, choices=[('项目监管周报', '项目监管周报'), ('项目监管月度分析', '项目监管月度分析'), ('行业情况通报', '行业情况通报'), ('分析报告', '分析报告')], max_length=30, null=True, verbose_name='报告类型'),
        ),
        migrations.AddField(
            model_name='reportuser',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ewproject.ewReport', verbose_name='报告'),
        ),
        migrations.AddField(
            model_name='reportuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='reportresource',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ewproject.ewReport', verbose_name='报告'),
        ),
    ]
