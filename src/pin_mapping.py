# This file contains PIN mappings to be used on LePotato

GPIOCHIP = "gpiochip1"
"""Constant that contains the name of the GPIO chip on the SBC. As default, this
is set to the 40-pin GPIO chip of LibreComputer's "Le Potato".
"""

# PIN dictionary from GPIO pin Name to Linux number
PIN_NAME = {
    "GPIOA9_5": 5,
    "GPIOAO_4": 4,
    "GPIOCLK_0": 98,
    "GPIOAO_8": 8,
    "GPIOAO_9": 9,
    "GPIOX_8": 87,
    "GPIOX_9": 88,
    "GPIOX_11": 90,
    "GPIODV_26": 75,
    "GPIOX_17": 96,
    "GPIOX_18": 97,
    "GPIOX_6": 85,
    "GPIOX_7": 86,
    "GPIOX_5": 84,
    "GPIOX_12": 91,
    "GPIOX_13": 92,
    "GPIOAO_6": 6,
    "GPIOX_14": 93,
    "GPIOX_15": 94,
    "GPIOX_0": 79,
    "GPIOX_10": 89,
    "GPIOX_1": 80,
    "GPIODV_27": 76,
    "GPIOX_16": 95,
    "GPIOX_2": 81,
    "GPIOX_3": 82,
    "GPIOX_4": 83,
}
"""Dictionary with GPIO pin names as keys and Linux pin number as values.
"""
