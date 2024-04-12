from machine import Pin, I2C
import ssd1306

i2c = I2C(1, scl=Pin(15), sda=Pin(14))

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

lines = []

while True:
    user_input = input()

    lines.append(user_input)

    if len(lines) > 8:
        lines.pop(0)

    oled.fill(0)

    for i, line in enumerate(lines):
        oled.text(line, 0, i*8)

    oled.show()

