from machine import ADC, Pin
import time

# Pin AO conectado a GPIO32
adc = ADC(Pin(32))

def leer_sensor():
    valor = adc.read()
    return valor

while True:
    calidad_aire = leer_sensor()
    print("Calidad del aire:", calidad_aire)
    time.sleep(1)