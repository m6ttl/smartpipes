# # from .mqttsub import func_run, on_mqtt_connect, on_message_come, on_subscribe, on_publish, talk, ew_MQTT_m2m, ew_MQTT_decode, ew_MQTT_app, ew_MQTT_p2p, ew_MQTT
from .mqttsub import func_run, on_mqtt_connect, on_message_come, on_subscribe, on_publish, talk


on_mqtt_connect()
on_subscribe()
print('MQTT start  OK')




