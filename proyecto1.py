import BlynkLib
import network
from time import sleep
from dht import DHT11
from machine import ADC, Pin, SPI
from ili9341 import Display
import machine
import time




# Configuración de los pines
rf_pin = machine.Pin(0, machine.Pin.IN)
adc = ADC(Pin(32))

def leer_sensor():
    valor = adc.read()
    return valor


 

# Inicialización de Blynk
BLYNK_AUTH = 'g7rmoDqKKGmGHgrxBmFB3LCetMUr2tDw'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Pines a utilizar
sensorDHT = DHT11(Pin(23))
sensor_pin = Pin(16, Pin.IN, Pin.PULL_UP)
led_pin = Pin(15, Pin.OUT)

spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(2))
display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))

# Conexión WiFi
def do_connect(nombre='PEINADO CORTEZ', contra='77169759'):
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a', nombre, '...')
        wlan.connect(nombre, contra)
        while not wlan.isconnected():
            pass
    print('Configuración de red:', wlan.ifconfig())

# Conexión a Blynk
do_connect()

# Función para encender o apagar el LED según el valor recibido de Blynk
def actualizar_led(valor):
    if int(valor[0]) == 1:
        led_pin.value(1)
    else:
        led_pin.value(0)

blynk.on("V0", actualizar_led)

# Función para medir la lluvia
def medir_lluvia():
    return not sensor_pin.value()

# Función para actualizar los sensores y enviar datos a Blynk
def update_sensors():
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    lluvia = "Esta lloviendo" if medir_lluvia() else "No hay lluvia"
    calidad_aire = leer_sensor()
    blynk.virtual_write(1, temp)
    blynk.virtual_write(2, hum)
    blynk.virtual_write(3, calidad_aire)
    blynk.virtual_write(4, lluvia)
    
    # Se pasa a String y se imprime en la pantalla led
    temp_string = str(temp)
    calidad_aire_string = str(calidad_aire)
    display.draw_text8x8(0, 0, "Temperatura: " + temp_string, 0xFFFFFF)
    hum_string = str(hum)
    display.draw_text8x8(0, 50, "Humedad: " + hum_string, 0xFFFFFF)
    display.draw_text8x8(0, 100, "Clima: " + lluvia, 0xFFFFFF)
    display.draw_text8x8(0, 150, "Calidad del aire : " + calidad_aire_string, 0xFFFFFF)
    print(temp_string + " " + hum_string + " " + lluvia + " "+ calidad_aire_string)

# Función para recibir señal
def recibir_senal():
    
    if rf_pin.value() == 1:
        print("Señal recibida")
        led_pin.value(1)
        print(rf_pin.value())
        
    else:
        print("Señal recibida")
        print(rf_pin.value())

    


while True:
    blynk.run()
    update_sensors()
    sleep(2)
