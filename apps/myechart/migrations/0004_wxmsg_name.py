# Generated by Django 2.0.1 on 2019-03-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechart', '0003_wxmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='wxmsg',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='标题'),
        ),
    ]
