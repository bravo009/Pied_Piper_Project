#! /usr/bin/python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

broker_address="192.168.1.109" # IP address of local broker
print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker


LedPin = 15    # pin15

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
    GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led
    GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(18,GPIO.IN)


def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource
    print(" - I have run the cleanup function -")


def checkdist():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(16, GPIO.LOW)
    while not GPIO.input(18):
        pass
    t1 = time.time()
    while GPIO.input(18):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

time.sleep(2)

try:
        setup()
        while True:
            d = checkdist()
            print 'Distance: %0.2f m' %d
            if d > 1:
                print '...led on'
                GPIO.output(LedPin, GPIO.LOW)  # led on
                client.publish("test", "Parking Available")
                time.sleep(0.5)
            else:
                print '...led off'
                GPIO.output(LedPin, GPIO.HIGH) # led off
                client.publish("test", "Parking Occupied")
                time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()

