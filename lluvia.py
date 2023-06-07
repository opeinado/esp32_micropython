import machine
import time

# Pin DO conectado a GPIO16
sensor_MH = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)


def medir_lluvia():
    return not sensor_MH.value()

while True:
    if medir_lluvia():
        print("¡Está lloviendo!")
    else:
        print("No hay lluvia")
    time.sleep_ms(500)
