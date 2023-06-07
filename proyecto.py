#https://ny3.blynk.cloud/external/api/update?token=RMPE88QDCZPztMho8s6zf7y1EUG-3l4W&V0=1
import BlynkLib, network
from time import sleep
from dht import DHT11
from machine import Pin, SPI
from ili9341 import Display


#pines a utilizar
sensorDHT = DHT11(Pin(22))
sensor_pin = Pin(16, Pin.IN, Pin.PULL_UP)
led_pin = Pin(2, Pin.OUT)

spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))



#Conexion Wifi
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


#Conexion a Blynk
do_connect()
BLYNK_AUTH = 'RMPE88QDCZPztMho8s6zf7y1EUG-3l4W'


#inialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
n = 0
v = 1

def read_dht11():
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    return (temp,hum)

# Función para encender o apagar el LED según el valor recibido de Blynk
def actualizar_led(valor):
    if int(valor[0]) == 1:
        led_pin.value(1)
    else:
        led_pin.value(0)
        

blynk.on("V0", actualizar_led)


        
# Función para detectar si está lloviendo        
def medir_lluvia():
    return not sensor_pin.value()

def update_sensors():
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    lluvia = "Esta lloviendo" if medir_lluvia() else "No hay lluvia"
    blynk.virtual_write(1, temp)
    blynk.virtual_write(2, hum)
    blynk.virtual_write(4, lluvia)
# se pasa a String y se imprime en la pantalla led    
    temp_string = str(temp)
    display.draw_text8x8(0, 0, "Temperatura: " + temp_string, 0xFFFFFF)
    hum_string = str(hum)
    display.draw_text8x8(0, 50, "Humedad: " +hum_string, 0xFFFFFF)
    display.draw_text8x8(0, 100, "Clima: " +lluvia, 0xFFFFFF)
    
  
while True:
    
    blynk.run()
    update_sensors()
    sleep(3)
    