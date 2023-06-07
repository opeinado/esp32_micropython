from machine import ADC, Pin
import time

adc = ADC(Pin(32))

def sensor_mq135():
    valor = adc.read()
    return valor

while True:
    calidad_aire = sensor_mq135()
    print("Calidad del aire:", calidad_aire)
    time.sleep(2)
