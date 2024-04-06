from libraries.sr74hc595n import Sr74hc595n
from time import sleep


# Pins for the Shift Register
# Data:     GP11
# Clock:    GP12
# Latch:    GP13
# ~Clear:   GP14
# ~OE:      GP15
sr = Sr74hc595n(data=11, clock=12, latch=13, clear=14, out_enable=15)


def main():
    sr.write(0b10101010)
    for i in range(0, 100, 10):
        sr.brightness(i)
        sleep(0.5)
    for i in range(100, 0, -10):
        sr.brightness(i)
        sleep(0.5)
    sr.brightness(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sr.deinit()
