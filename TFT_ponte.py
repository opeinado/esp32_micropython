"""ILI9341 demo (images)."""
import time
from ili9341 import Display
from machine import Pin, SPI, ADC

adc = ADC(Pin(15))
adc.atten(ADC.ATTN_11DB)

# PINES 
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(2))
display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))

def test():
    """Test code."""
    
    
    potensiometro_int = adc.read()
    print(potensiometro_int)
    potensiometro_string = str(potensiometro_int)
    display.draw_text8x8(0, 50, potensiometro_string, 0xFFFFFF)


    display.draw_text8x8(0, 0, "hola mundo", 0xFFFFFF)
    

    

while True:
    
    time.sleep_ms(100)
    test()
