#SENSOR FBD-RX01A (RF) 433 hz

import machine
import time

rf_pin = machine.Pin(0, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)

while True:
    if rf_pin.value() == 1 :
        print ("señal resibida led encendido")
        led.value(1)
        time.sleep(3)
        
    else:
        print ("led apagado")
        led.value(0)
        time.sleep(3)
        
        