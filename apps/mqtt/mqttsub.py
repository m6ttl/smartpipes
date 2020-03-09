import simplejson as json
import numpy as np
import pandas as pd
from pandas import DataFrame
import pymysql
# from pandasql import sqldf
import json
from pandas.io.json import json_normalize
import records

import time
from datetime import datetime
import datetime

import paho.mqtt.client as mqtt
from multiprocessing import Process

# MQTTHOST = "127.0.0.1"
MQTTHOST = "47.110.40.193" #阿里云
# 公网： 47.110.40.193
# 私有IP： 172.16.8.71

MQTTPORT = 1883
g_topic = 'Ew/#'

# Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
mqttClient = mqtt.Client()
mqtt_sql_s = 'mysql+pymysql://root_top:root_Top@rm-uf6k42ke05jq7358so.mysql.rds.aliyuncs.com:3306/smartpipe?charset=utf8'

db = records.Database(mqtt_sql_s)

## 1. 物联网解析
# topic定义：Ew/m2m/厂家/类型/版本/注册设备编号

def ew_MQTT_m2m(as_topic, as_code):
    is_decode_str = 'ERR: 没有找到那个消息'
    i_topic = as_topic
    is_in = as_code
    is_t = i_topic.split('/', 2)[2]
    is_vendor, is_model, is_ver, is_client = is_t.split('/', 4)

    db = records.Database(mqtt_sql_s)
    if is_vendor == 'ewide':
        if is_model == 'smartpipe':
            if is_ver == 'JV1':
                list_ins = json.loads(is_in)  # json读取
                df_run = json_normalize(list_ins)  # json 转 dataframe

                # 通过编号得到ID
                sql_pipe_id = "SELECT id FROM smartpipe_smartpipe where sn = '{}'".format(is_client)
                rows = db.query(sql_pipe_id)
                i_pipe_id = rows[0]['id']  # 设备ID

                # 整理插入df
                df_run["pipe_id_id"] = i_pipe_id
                df_run1 = df_run[["pipe_id_id", "collection_time", "pressure", "ins_flow", "tem", "power"]] \
                    .to_json(orient="records", force_ascii=False)

                # 转换list
                list_run1 = json.loads(df_run1)

                # 执行插入
                t_sql = "insert smartpipe_pipedetail(pipe_id_id, collection_time,pressure, ins_flow, tem, power ) \
                               values (:pipe_id_id, :collection_time, :pressure, :ins_flow, :tem, :power) "
                db.bulk_query(t_sql, list_run1)

                return 'OK ewide smartpipe run'

    return is_decode_str

## 2.解码消息传递
def ew_MQTT_decode(as_topic, as_code):
    is_decode_str = 'OK'

    return is_decode_str

## 3. 应用消息服务
# topic定义：Ew/app/项目/服务编号/版本/源消息用户号

def ew_MQTT_app(as_topic, as_code):
    is_decode_str = 'ERR: 没有找到那个app消息'
    i_topic = as_topic
    is_in = as_code
    is_t = i_topic.split('/', 2)[2]
    is_prj, is_event, is_ver, isclient = is_t.split('/', 4)

    db = records.Database(mqtt_sql_s)
    if is_event == 'ppIns':
        if is_ver == 'JV1':
            list_ins = json.loads(is_in)  # json读取
            df_ins = json_normalize(list_ins)  # json 转 dataframe

            i_sn = df_ins['sn'].iloc[0]  # 设备编号
            i_project_id = df_ins['project_id'].iloc[0]  # 项目编号
            i_name = df_ins['name'].iloc[0]  # 名称 一般记录的是地名
            i_depth = df_ins['depth'].iloc[0]  # 埋深
            i_interface = df_ins['interface'].iloc[0]  # 接口形式
            i_longitude = df_ins['longitude'].iloc[0]  # 经度
            i_latitude = df_ins['latitude'].iloc[0]  # 纬度

            sql_out = """\
            update smartpipe_smartpipe t SET \
            project_id = {},\
            install_date = sysdate(),\
            name = '{}',\
            depth = {},\
            interface = '{}',\
            longitude = {},\
            latitude = {} \
            where sn = '{}'\
            """.format(i_project_id, i_name, i_depth, i_interface, i_longitude, i_latitude, i_sn)

            db.query(sql_out)

            return 'OK: ppIns'

    return is_decode_str

## 4. 点对点消息服务
def ew_MQTT_p2p(as_topic, as_code):
    is_decode_str = 'OK'

    return is_decode_str

## 消息分发服务
def ew_MQTT(as_topic, as_code):
    i_topic = as_topic
    is_in = as_code
    print(i_topic)

    is_top = i_topic.split('/', 1)[0]
    if is_top != 'Ew':
        is_decode_str = 'ERR: 消息不合法'
        return is_decode_str

    is_decode_str = 'ERR: 没有找到那个消息'
    is_kind = i_topic.split('/', 2)[1]
    if is_kind == 'm2m':
        is_decode_str = ew_MQTT_m2m(as_topic, as_code)
    if is_kind == 'decode':
        is_decode_str = ew_MQTT_decode(as_topic, as_code)
    if is_kind == 'app':
        is_decode_str = ew_MQTT_app(as_topic, as_code)
    if is_kind == 'p2p':
        is_decode_str = ew_MQTT_p2p(as_topic, as_code)

    sql_log = """ INSERT INTO mqtt_submsg SET name = unix_timestamp(now()), topic = '{}', subtime = sysdate(), payload = '{}' """ \
        .format(as_topic, as_code)
    db.query(sql_log)

    return is_decode_str


## MQTT 服务
# 连接MQTT服务器
def on_mqtt_connect():
    # connect(host, port=1883, keepalive=60, bind_address="")
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# 消息处理函数
# def on_message_come(lient, userdata, msg):
#     try:
#         cursor = conn.cursor()
# #         sql = """ INSERT INTO mqtt_submsg SET topic = '%s', subtime = sysdate(), payload = '%s' """ % (msg.topic,str(msg.payload.decode("utf-8")))

#         sql = """ INSERT INTO mqtt_submsg SET topic = :topic, subtime = sysdate(), payload = :payload """

#         cursor.execute(sql,
#                        params={'tppic':msg.topic,
#                                'payload':str(msg.payload.decode("utf-8"))})
#         conn.commit()
#         cursor.close()
#         print ("=  插入成功  ="  )
#         return 1

#     except Exception as e:
#         print ("*  插入失败    *"  + sql)
#         print (e)
#         return 0


#     print('sql:' + sql)
# 消息处理开启多进程
#     p = Process(target=talk, args=("/camera/person/num/result", msg.payload.decode("utf-8")))
#     p.start()


# # 消息处理函数
# def on_message_come(lient, userdata, msg):
#     try:
#         cursor = conn.cursor()
#         sql_log = """ INSERT INTO mqtt_submsg SET name = unix_timestamp(now()), topic = '%s', subtime = sysdate(), payload = '%s' """ % (msg.topic,str(msg.payload.decode("utf-8")))
#         cursor.execute(sql_log)
#         sql_do = ew_decode(msg.topic, str(msg.payload.decode("utf-8")))
#         cursor.execute(sql_do)
#         conn.commit()
#         cursor.close()
# #         print ("=  插入成功  =" + msg.topic + str(msg.payload.decode("utf-8")))
#         print ("=  插入成功  =" + sql_do)

# #         print(sql_do)
#         return 1

#     except Exception as e:
#         print ("*  插入失败    *"  + sql_log)
#         print (e)
#         return 0

# 消息处理函数
def on_message_come(lient, userdata, msg):
    # print("decode:" + msg.topic + str(msg.payload.decode("utf-8")))
    i_do = ew_MQTT(msg.topic, str(msg.payload.decode("utf-8")))
    print(i_do)

# subscribe 消息订阅
def on_subscribe():
    mqttClient.subscribe(g_topic, 1)  # 主题为"Ew/...."
    mqttClient.on_message = on_message_come  # 消息到来处理函数


# publish 消息发布
# publish(topic, payload=None, qos=0, retain=False)
def on_publish(topic, msg, qos):
    mqttClient.publish(topic, msg, qos);


# 多进程中发布消息需要重新初始化mqttClient
def talk(topic, msg):
    cameraPsersonNum = camera_person_num.CameraPsersonNum(msg)
    t_max, t_mean = cameraPsersonNum.personNum()
    mqttClient = mqtt.Client()
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()
    mqttClient.publish(topic, '{"max":' + str(t_max) + ',"mean:"' + str(t_mean) + '}', 1)

## 启动 MQTT 服务
# 订阅
# on_mqtt_connect()
# on_subscribe()
#
# print('start OK')

## 停止 MQTT 服务
# 弄完了
# # cursor.close()
# mqttClient.loop_stop()
# print('stop OK')

# 测试启动情况
def func1():
	a = '111111'
	print(a)
def func2():
	b = '222222'
	print(b)
def func_run():
	func1()
	func2()

# func_run()
