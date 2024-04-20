#################################################
# Wrapper class for the LED Display             #
# Lino Oropeza                                  #
# 2024                                          #
#################################################

# Libraries needed
from lib.sr74hc595n import Sr74hc595n


class LedDisplay:
    # The anode and cathodes are given as dictionaries
    # The dictionaries are populated with info to use the Shift Registers
    # The dictionaries contain
    #   data:       data pin
    #   clock:      clock pin
    #   latch:      latch pin
    #   clear:      clear register pin
    #   oe:         output enable
    #   led_count:  number of leds connected to the shift register.
    #               It should be a number divided by 8
    def __init__(self, anode_pins: dict, cathode_pins: dict) -> None:
        pass
