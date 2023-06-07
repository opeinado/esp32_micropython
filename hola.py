"""ILI9341"""
import time
from ili9341 import Display
from machine import ADC,Pin, SPI




"""Test code."""

# Baud rate of 40000000 seems about the max
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(2))
display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))

adc = ADC(Pin(15))
adc.atten(ADC.ATTN_11DB)

while True:
    potensiometro_int = adc.read()
    print(potensiometro_int)
    potensiometro_string = str(potensiometro_int)
    display.draw_text8x8(0, 0, potensiometro_string, 0xFFFFFF)
    time.sleep_ms(100)
    
    