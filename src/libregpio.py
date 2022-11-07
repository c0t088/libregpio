""" 
Importing the module
====================

To import the libregpio module:

```python
import libregpio as GPIO
```
This way allows you to refer to it as GPIO for the rest of your program.

PIN Numbering
=============
To access the 40-pin GPIO via *gpiod* is required to use the Linux pin number. The libregpio module uses a dictionary, so the pins are initialized by the Name in its functions.

Please, see Libre Computer's GPIO Headers Reference: https://docs.google.com/spreadsheets/d/1U3z0Gb8HUEfCIMkvqzmhMpJfzRqjPXq7mFLC-hvbKlE/edit#gid=0
"""
from pin_mapping import GPIOCHIP, PIN_NAME
from os import system, popen


class OUT:
    """This is a class representantion of a GPIO pin to be used as an output.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    """    
    def __init__(self, pin):
        self.pin = PIN_NAME[pin]

    def output(self, value):
        """Set an output value to a libregpio.OUT object (i.e. 0 or 1).

        :param value: output value to be sent to GPIO pin
        :type value: int
        """        
        self.value = value
        if self.value in [0, 1]:
            system(f"gpioset {GPIOCHIP} {self.pin}={self.value}")

    def LOW(self):
        """Set a value of 0 to a libregpio.OUT object"""   
        system(f"gpioset {GPIOCHIP} {self.pin}=0")

    def HIGH(self):
        """Set a value of 1 to a libregpio.OUT object."""
        system(f"gpioset {GPIOCHIP} {self.pin}=1")

    def active_low(self):
        """Set libregpio.OUT object to active_low."""
        system(f"gpioset {GPIOCHIP} {self.pin} -l")
    
    def toggle(self):
        """Toggle output value of a GPIO pin
        
        When current value is greater than 1 change to 0, Else, change to 1."""
        current_value = int(popen(f"gpioget {GPIOCHIP} {self.pin}").read())
        if current_value > 0:
            self.LOW
        else:
            self.HIGH


class IN:
    """This is a class representantion of a GPIO pin to be used as an input.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    """  
    def __init__(self, pin):
        self.pin = PIN_NAME[pin]

    def input(self):
        """Read an input value from a libregpio.IN object.

        :return: Input value read from GPIO pin (i.e. 0 or 1)
        :rtype: int
        """        
        value = int(popen(f"gpioget {GPIOCHIP} {self.pin}").read())
        return value

""" 
Global Methods
==============
"""

def cleanup():
    """Set a 0 value to every GPIO pin. It is a good practice to call this function at the end of your program to prevent shorting pins.
    """    
    for pin in PIN_NAME.values():
        system(f"gpioset {GPIOCHIP} {pin}=0")
