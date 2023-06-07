from machine import Pin, ADC
from time import sleep

sensor_HW = ADC(Pin(15))
led = Pin(2, Pin.OUT)
sensor_HW.atten(ADC.ATTN_11DB)
sensor_HW.width(ADC.WIDTH_12BIT)
while True:
    valor = sensor_HW.read()
    voltaje = (3.3 / ((2**12)-1)) *valor
    print (voltaje)
    if (voltaje>1.482):
        led.value(True)
    else:
        led.value(False)
    sleep(0.2)