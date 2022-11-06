from pin_mapping import GPIOCHIP, PIN_NAME
from os import system, popen


class OUT:
    def __init__(self, pin):
        self.pin = PIN_NAME[pin]

    def output(self, value):
        """Send an output to a GPIO pin.

        Set an output value to a libregpio.OUT object (i.e. 0 or 1).

        Parameters
        ----------
        value : int
            output value (0 or 1)
        """
        self.value = value
        if self.value in [0, 1]:
            system(f"gpioset {GPIOCHIP} {self.pin}={self.value}")

    def LOW(self):
        """Set a value of 0 to a libregpio.OUT object."""
        system(f"gpioset {GPIOCHIP} {self.pin}=0")

    def HIGH(self):
        """Set a value of 1 to a libregpio.OUT object."""
        system(f"gpioset {GPIOCHIP} {self.pin}=1")

    def active_low(self):
        """Set libregpio.OUT object to active_low."""
        system(f"gpioset {GPIOCHIP} {self.pin} -l")


class IN:
    def __init__(self, pin):
        self.pin = PIN_NAME[pin]

    def input(self):
        """Read input from a GPIO pin

        Read an input value from a LibreGPIO.IN object.

        Returns
        -------
        value : int
            Input value read from GPIO pin (i.e. 0 or 1)
        """
        value = int(popen(f"gpioget {GPIOCHIP} {self.pin}").read())
        return value


def cleanup():
    for pin in PIN_NAME.values():
        """Set all GPIO pins to Low.

        Set a 0 value to every GPIO pin in `pin_mapping.py`.

        """
        system(f"gpioset {GPIOCHIP} {pin}=0")
