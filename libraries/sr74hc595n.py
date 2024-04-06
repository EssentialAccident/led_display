#################################################
# Wrapper class for the Shift Register 74HC595N #
# Lino Oropeza                                  #
# 2024                                          #      
#################################################

from machine import Pin
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
        #                   when pulled low
        
        self.data = Pin(data, Pin.OUT)
        self.clock = Pin(clock, Pin.OUT)
        self.latch = Pin(latch, Pin.OUT)
        self.clear_register = Pin(clear, Pin.OUT)
        self.out_enable = Pin(out_enable, Pin.OUT)
        self.num_registers = num_registers

        # Setting the initial states of the Shift Register pins
        self.data.off()
        self.clock.off()
        self.latch.off()
        self.clear_register.on()
        self.out_enable.off()

        # Set up the register
        self.clear_register()


    def clear(self) -> None:
        # It clears the shift register
        self.clear_register.off()
        self.clear_register.on()
        self.__pulse_latch()

    def outputs_enable(self, value: bool) -> None:
        if value:
            self.out_enable.off()
        if not value:
            self.out_enable.on()

    def outputs_enable_toggle(self) -> None:
        self.out_enable.toggle()

    def __pulse_clock(self) -> None:
        self.clock.on()
        self.clock.off()

    def __pulse_latch(self) -> None:
        self.latch.on()
        self.latch.off()
        

    def write(self, data: int) -> None:
        for i in range(self.num_registers * 8):
            bit = (data >> i) & 1
            self.data.value(bit)
            self.__pulse_clock()
        self.__pulse_latch()

