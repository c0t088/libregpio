from pin_mapping import GPIOCHIP, PIN_NAME
from os import system, popen


class OUT:
    """This is a class representantion of a GPIO pin to be used as an output.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    :type pin: string
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

    def low(self):
        """Set a value of 0 to a libregpio.OUT object"""   
        system(f"gpioset {GPIOCHIP} {self.pin}=0")

    def high(self):
        """Set a value of 1 to a libregpio.OUT object."""
        system(f"gpioset {GPIOCHIP} {self.pin}=1")

    def active_low(self):
        """Set libregpio.OUT object to active_low."""
        system(f"gpioset {GPIOCHIP} {self.pin} -l")
    
    def toggle(self):
        """Toggle output value of a GPIO pin"""
        current_value = int(popen(f"gpioget {GPIOCHIP} {self.pin}").read())
        self.output(int(not(current_value)))


class IN:
    """This is a class representantion of a GPIO pin to be used as an input.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    :type pin: string
    """  
    def __init__(self, pin):
        self.pin = PIN_NAME[pin]

    def input(self, bias="as-is"):
        """Read an input value from a libregpio.IN object.

        This method can read the pin input value at a given time.

        Use the bias parameter to enable pull-up or pull-down modes.

        :param bias: ``pull-up`` ``pull-down`` ``as-is`` ``disable``
        :type bias: string, optional
        :return: Input value read from GPIO pin (i.e. 0 or 1)
        :rtype: int
        """        
        value = int(popen(f"gpioget -B {bias} {GPIOCHIP} {self.pin}").read())
        return value
    
    def wait_for_edge(self, edge='rising', num_events=1, active_low=False):
        """Returns an input value when a specific edge event is detected. This method is designed to stop your program execution until an event is detected.

        :param edge: Type of event to wait for (``rising`` ``falling``), defaults to 'rising'
        :type edge: str, optional
        :param num_events: number of events to wait for. defaults to 1
        :type num_events: int, optional
        :param active_low: Set pin to active-low state (``True`` ``False``). defaults to False.
        :type num_events: Boolean, optional
        :return: ``1`` for rising.`0`for falling
        :rtype: int
        """
        if active_low:
            al = '-l'
        else:
            al = ''

        for event in range(num_events):
            if edge == 'rising':
                edge_val = int(popen(f'gpiomon -r -n 1 {al} -B pull-down -F "%e" {GPIOCHIP} {self.pin}').read())
            elif edge == 'falling':
                edge_val = int(popen(f'gpiomon -f -n 1 {al} -B pull-up -F "%e" {GPIOCHIP} {self.pin}').read())
            else:
                edge_val = None
        return edge_val


def cleanup():
    """Set a 0 value to every GPIO pin. It is a good practice to call this function at the end of your program to prevent shorting pins.
    """    
    for pin in PIN_NAME.values():
        system(f"gpioset {GPIOCHIP} {pin}=0")
