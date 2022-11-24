from pin_mapping import PIN_NAME
from os import system, popen
from threading import Thread
from time import sleep


class OUT:
    """This is a class representantion of a GPIO pin to be used as an output.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    :type pin: str
    """    
    def __init__(self, pin):
        self.GPIOCHIP = set_chip(pin)
        self.pin = PIN_NAME[pin]
    
    def output(self, value):
        """Set an output value to a libregpio.OUT object (i.e. ``0`` or ``1``).

        :param value: output value to be sent to GPIO pin
        :type value: int
        """        
        self.value = value
        if self.value in [0, 1]:
            system(f"gpioset {self.GPIOCHIP} {self.pin}={self.value}")

    def low(self):
        """Set a value of ``0`` to a libregpio.OUT object"""   
        system(f"gpioset {self.GPIOCHIP} {self.pin}=0")

    def high(self):
        """Set a value of ``1`` to a libregpio.OUT object."""
        system(f"gpioset {self.GPIOCHIP} {self.pin}=1")

    def active_low(self):
        """Set libregpio.OUT object to active_low."""
        system(f"gpioset {self.GPIOCHIP} {self.pin} -l")
    
    def toggle(self):
        """Toggle output value of a GPIO pin"""
        current_value = int(popen(f"gpioget -B disable {self.GPIOCHIP} {self.pin}").read())
        self.output(int(not(current_value)))


class IN:
    """This is a class representantion of a GPIO pin to be used as an input.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    :type pin: str
    """  
    def __init__(self, pin):
        self.GPIOCHIP = set_chip(pin)
        self.pin = PIN_NAME[pin]

    def input(self, bias="as-is"):
        """Read an input value from a libregpio.IN object.

        This method can read the pin input value at a given time.

        Use the bias parameter to enable pull-up or pull-down modes.

        :param bias: ``pull-up``, ``pull-down``, ``as-is``, ``disable``
        :type bias: str, optional
        :return: Input value read from GPIO pin (i.e. ``0`` or ``1``)
        :rtype: int
        """        
        value = int(popen(f"gpioget -B {bias} {self.GPIOCHIP} {self.pin}").read())
        return value
    
    def wait_for_edge(self, bias="as-is", edge='rising', num_events=1, active_low=False):
        """Returns an input value when a specific edge event is detected. This method is designed to stop your program execution until an event is detected.

        :param bias: ``pull-up``, ``pull-down``, ``as-is``, ``disable``
        :type bias: str, optional
        :param edge: Type of event to wait for (``rising``, ``falling``), defaults to 'rising'
        :type edge: str, optional
        :param num_events: number of events to wait for. defaults to 1
        :type num_events: int, optional
        :param active_low: Set pin to active-low state (``True``, ``False``). defaults to False.
        :type num_events: Boolean, optional
        :return: ``1`` for rising ``0`` for falling
        :rtype: int
        """
        if active_low:
            al = '-l'
        else:
            al = ''

        for event in range(num_events):
            if edge == 'rising':
                edge_val = int(popen(f'gpiomon -r -n 1 {al} -B {bias} -F "%e" {self.GPIOCHIP} {self.pin}').read())
            elif edge == 'falling':
                edge_val = int(popen(f'gpiomon -f -n 1 {al} -B {bias} -F "%e" {self.GPIOCHIP} {self.pin}').read())
            else:
                edge_val = None
        return edge_val


class PWM(Thread):
    """This is a class representantion of a GPIO pin to be used as an PWM output.

    Use only with pins compatible with PWM (pulse width modulation).

    Creating the class instance does not automatically sends a PWM output.

    :param pin: GPIO pin name (i.e. GPIOX_4)
    :type pin: str
    :param duty_cycle: duty cycle percentage
    :type duty_cycle: int
    :param freq: frequency in Hertz
    :type freq: float
    """ 

    def __init__(self, pin, duty_cycle, freq):
        self.GPIOCHIP = set_chip(pin)
        self.pin_name = pin
        self.pin = PIN_NAME[pin]
        self.duty_cycle = duty_cycle
        self.max_cycle = 100.0
        self.pulse_time = 1.0/freq
        self.slice = self.pulse_time / self.max_cycle
        self.to_stop = False
        self.stopped = False

    def pulse_loop(self):
        """This method is called by ``start()`` to loop the pulse output on a different thread

        Do not call this method outside of this class.
        """
        while self.to_stop == False:
            system(f"gpioset {self.GPIOCHIP} {self.pin}=1")
            sleep(self.duty_cycle * self.slice)
            system(f"gpioset {self.GPIOCHIP} {self.pin}=0")
            sleep((self.max_cycle - self.duty_cycle) * self.slice)
        self.stopped = True

    def start(self, duty_cycle=None):
        """Start the PWM output.

        You can update the duty cycle when starting this method.

        :param duty_cycle: duty cycle percentage, defaults to None
        :type duty_cycle: int, optional
        """
        if duty_cycle:
            self.duty_cycle = duty_cycle
        self.thread = Thread(None, target=self.pulse_loop)
        self.thread.start()

    def stop(self):
        """Stop the PWM output

        It 'cleans up' the GPIO pin.
        """
        while self.stopped == False:
            self.to_stop = True
            sleep(0.01)
        cleanup([self.pin_name])

    def change_duty_cycle(self, duty_cycle):
        """Modify the current duty cycle

        :param duty_cycle: duty cycle percentage
        :type duty_cycle: int
        """
        self.duty_cycle = duty_cycle
    
    def change_freq(self, freq):
        """Modify the current frequency

        :param freq: frequency in Hertz
        :type freq: float
        """
        self.pulse_time = 1.0/freq
        self.slice = self.pulse_time / self.max_cycle


def cleanup(pins=None):
    """By Default, it sets all pins to ``0`` but you can pass a list if only specific pins need to be cleaned up.

    It is recommended to use this method at the end of your program.

    :param pins: list/tuple of pin or pins by name, defaults to ``None``
    :type pins: iterable, optional
    """
    if pins:
        for pin in pins:
            system(f"gpioset {set_chip(pin)} {PIN_NAME[pin]}=0")
    else:
        for pin in PIN_NAME.values():
            system(f"gpioset {set_chip(pin)} {pin}=0")


def set_chip(pin_name):
    """Select the gpio chip corresponding to the pin. Do not call this function.

    :param pin_name: gpio pin name
    :type pin_name: str
    :return: gpio chip
    :rtype: str
    """
    chip_zero = ['GPIOAO_5','GPIOAO_4','GPIOAO_8','GPIOAO_9','TEST_N','GPIOAO_6']
    if pin_name in chip_zero:
        chip = 0
    else:
        chip = 1
    return str(chip)
