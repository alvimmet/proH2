import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

buttonup = Pin(7, Pin.IN, Pin.PULL_UP)   
buttondown = Pin(9, Pin.IN, Pin.PULL_UP)  
buttonclear = Pin(8, Pin.IN, Pin.PULL_UP) #if I use pin10 of rotar(ROTA) then it's more funtionable

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

x = 0
y = display.height // 2

def line_making():
    global x, y
    display.pixel(x, y, 1)
    display.show()
    x += 1
    if x >= display.width:
        x = 0

while True:
    line_making()
    time.sleep(0.01) 

    if not buttonup.value():  
        y = max(0, y - 1)  
    if not buttondown.value():  
        y = min(display.height - 1, y + 1)  
    if not buttonclear.value(): 
        display.fill(0)  
        y = display.height // 2 
        x = 0  
