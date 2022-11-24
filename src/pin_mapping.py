# PIN dictionary from GPIO pin Name to Linux number
PIN_NAME = {
    "GPIOAO_5": 5,
    "GPIOAO_4": 4,
    "GPIOCLK_0": 98,
    #* Requires 2J1 jumper to be positioned to pass GPIOAO_8 to 40 pin header. 
    # Default is set to HDMI CEC. Move the jumper to the two pins on the edge of the board for 
    # controlling GPIO on the 40 pin header.
    #"GPIOAO_8": 8,
    "GPIOAO_9": 9,
    #Output only pin. This pin can be set to input and pulled down to reset the system.
    #"TEST_N":10,
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
