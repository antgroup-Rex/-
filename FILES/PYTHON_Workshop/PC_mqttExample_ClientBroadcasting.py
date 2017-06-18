import paho.mqtt.client as mqtt
print dir (mqtt)

import time

####################################
mqttc = mqtt.Client()
mqttc.connect("iot.eclipse.org")
mqttc.loop_start()
i=0

while True:
    i=i+1
    temperature = i#sensor.blocking_read()
    # res=mqttc.publish("paho/temperature", temperature)
    res=mqttc.publish("myNewRan", temperature)
    if res[0]!=0:
        print"possible publish error"
    # print i, res
    time.sleep(0.5)

##########################################
from umqtt.simple import MQTTClient
