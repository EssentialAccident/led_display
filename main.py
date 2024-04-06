# Micropython Libraries
from machine import Pin, I2C
from time import sleep

# Local Libraries
from lib.sr74hc595n import Sr74hc595n
from lib.i2c_lcd.pico_i2c_lcd import I2cLcd

# Setting up shift register
# Pins for the Shift Register
# Data:     GP11
# Clock:    GP12
# Latch:    GP13
# ~Clear:   GP14
# ~OE:      GP15
sr = Sr74hc595n(data=11, clock=12, latch=13, clear=14, out_enable=15)

# Setting up I2C and LCD Screen
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


def main():
    number = 1
    going_up = True
    while True:
        lcd.clear()
        sr.write(number)
        lcd.putstr(f'Writing: {number} \n{bin(number)}')
        sleep(0.2)
        if going_up:
            number = number * 2
        else:
            number = number //2
        if number > 2**6:
            going_up = False
        if number == 1:
            going_up = True
            number = 1
        


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sr.deinit()
        lcd.clear()
