#################################################
# Wrapper class for the Shift Register 74HC595N #
# Lino Oropeza                                  #
# 2024                                          #      
#################################################

from machine import Pin, PWM
from time import sleep

SLEEP_TIME = 0

class Sr74hc595n:
    def __init__(self, data: int, clock: int, latch: int, clear: int, out_enable: int , num_registers: int = 1) -> None:
        # self.data:        Data pin for the Shift Register
        # self.clock:       Clock to shift the register.
        #                   Shifts on the rising edge of the clock
        # self.latch:       It stores the data on the register
        # self.clear:       Sets all the register to 0
        #                   It clears the register when pulled low
        #                   For the normal operation of the register, 
        #                   it has to be pulled high
        # self.out_enable:  It disables the outputs of the shift register
        #                   when pulled low.
        #                   It will be configured as a PWM pin.
        
        # Creating pins
        self.data = Pin(data, Pin.OUT)
        self.clock = Pin(clock, Pin.OUT)
        self.latch = Pin(latch, Pin.OUT)
        self.clear_register = Pin(clear, Pin.OUT)
        self.num_registers = num_registers

        # Setting the initial states of the Shift Register pins
        self.data.off()
        self.clock.off()
        self.latch.off()
        self.clear_register.on()
        
        # The output enable pin will be setup as PWM
        self.pwm_freq = 5000
        pin_out_enable = Pin(out_enable, Pin.OUT)
        self.pwm_output = PWM(pin_out_enable, freq=self.pwm_freq, invert=True)       
        # The display will be always initialized full brightness
        self.brightness(100)

        # It will store the data
        self.bin_data = 0

        # Set up the register
        self.clear_register()


    def clear(self) -> None:
        # It clears the shift register
        self.clear_register.off()
        self.clear_register.on()
        self.__pulse_latch()

    def brightness(self, percent: int) -> None:
        # The duty cycle of the PWM is a range from 0 to 65535
        # Converting the percent enter to a 0 to 65535 range
        duty_cycle = int((percent / 100) * 65535)
        self.pwm_output.duty_u16(duty_cycle)

    def __pulse_clock(self) -> None:
        self.clock.on()
        self.clock.off()

    def __pulse_latch(self) -> None:
        self.latch.on()
        self.latch.off()
        

    def write(self, data: int) -> None:
        self.bin_data = data
        for i in range(self.num_registers * 8):
            bit = (data >> i) & 1
            self.data.value(bit)
            self.__pulse_clock()
        self.__pulse_latch()
    
    def deinit(self) -> None:
        self.clear()
        self.pwm_output.deinit()

