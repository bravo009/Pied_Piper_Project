import paho.mqtt.client as mqtt
import time
import redis

r = redis.Redis(host='', port='', password='')
#r = redis.Redis(host='127.0.0.1', port='6379')

def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    print("message received " + m)
    r.set('RPIvalue',m)
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)


broker_address="127.0.0.1"
print("creating new instance")
client = mqtt.Client("sub1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

while True:
    client.subscribe("test")
    time.sleep(1) # wait

client.loop_stop() #stop the loop

