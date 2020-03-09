# Generated by Django 2.0.1 on 2019-12-09 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartpipe', '0002_auto_20191209_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smartpipe',
            options={'verbose_name': '设计院', 'verbose_name_plural': '设计院'},
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='MQTT_version',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='RTU_id',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='accident_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='accident_hand',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='accident_pic',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='accident_result',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='accident_star',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='alert_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='alert_hand',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='alert_id',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='alert_result',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='alert_type',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='broker_address',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='broker_port',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='caliber',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='cancel_flag',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='check_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='check_file',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='check_spec',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='collection_min',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='collection_time',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='concact',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='conn_timeout',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='factory_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='flow_l',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='ins_flow',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='install_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='interface',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='label',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='msg_info',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='msg_sec',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='msg_time',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='order_p',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='owner_id',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='pipe_id',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='pipeline',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='po_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='po_info',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='power',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='power_low',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='pressure',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='pressure_high',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='pressure_low',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='profile_name',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='profile_type',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='profile_version',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='publish_item',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='tot_flow',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='turnup_date',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='turnup_lat',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='turnup_lon',
        ),
        migrations.RemoveField(
            model_name='smartpipe',
            name='vendor_id',
        ),
    ]
