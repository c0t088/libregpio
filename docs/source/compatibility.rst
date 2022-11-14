Compatibility with other boards
===============================

This module is designed to work with Libre Computer's "LePotato". However, it can be mapped to different boards if needed, provided they are work with ``gpiod``.

To achieve this, you need to modify the constants in the ``pin_mapping.py`` file to match your board.

.. code-block::

    # Set this value to your GPIO chip name
    GPIOCHIP = "gpiochip1"

    # Modify this dictionary to your preffered pin names and corresponding
    # linux number of said pins
    PIN_NAME = {
    "GPIOA9_5": 5,
    "GPIOAO_4": 4,
    "GPIOCLK_0": 98,
    "GPIOAO_8": 8,
    "GPIOAO_9": 9,
    "GPIOX_8": 87,
    "GPIOX_9": 88,
    .
    .
    .