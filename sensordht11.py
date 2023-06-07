from dht import DHT11
from machine import Pin
from time import sleep

sensorDHT = DHT11(Pin(23))

while True:
    
    sleep(1)

    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()

    print("T={:02d} ºC, H={:02d} %".format(temp, hum))
