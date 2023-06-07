from time import sleep
from ili9341 import Display
from machine import Pin, SPI


def test():
    """Test code."""
    # PINES 
    spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(2))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))


    display.draw_text8x8(0, 0, "hola mundo", 0xFFFFFF)
    

    


test()
