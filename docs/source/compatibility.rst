Compatibility with other boards
===============================

This module is designed to work with Libre Computer's "LePotato". However, it can be mapped to different boards if needed, provided they are work with ``gpiod``.

To achieve this, you need to modify the ``pin_mapping.py`` file to match your board.

.. code-block::

    # Modify this dictionary to your preffered pin names and corresponding
    # linux number of said pins
    PIN_NAME = {
    "GPIOAO_5": 5,
    "GPIOAO_4": 4,
    "GPIOCLK_0": 98,
    .
    .
    .

And you need to modify the ``set_chip()`` method in the ``libregpio.py`` file to set the corresponding chip of every pin.

.. code-block::

    def set_chip(pin_name):
    # modify this code to match your board gpio chips
        chip_zero = ['GPIOAO_5','GPIOAO_4','GPIOAO_8','GPIOAO_9','TEST_N','GPIOAO_6']
        if pin_name in chip_zero:
            chip = 0
        else:
            chip = 1
        return str(chip)