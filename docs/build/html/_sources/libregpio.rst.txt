Importing the module
====================

To import the libregpio module:

.. code-block:: python

       import libregpio as GPIO
       
This way allows you to refer to it as GPIO for the rest of your program.

PIN Reference
=============

This module is designed to work with the 40-pin chip of Libre Computer AML-S905X-CC "LePotato".

.. image:: gpio40pin-lepotato.png

.. note::
       Please, see Libre Computer's GPIO Headers Reference for full functions documentation: https://docs.google.com/spreadsheets/d/1U3z0Gb8HUEfCIMkvqzmhMpJfzRqjPXq7mFLC-hvbKlE/edit#gid=0

To access GPIO pins with this module, a class instance needs to be created. The pins are referred to by their GPIO name.

This is an example of an ``IN`` (input) class instance set to use 'GPIOX_4' pin:

.. code-block:: python

       import libregpio as GPIO

        a_pin = GPIO.IN('GPIOX_4')

How to use
==========

As noted in the previous section, GPIO pins are handled as class instances based on their intended use. Here we will run through some code examples.

.. note::
       Please, take notice that the ``cleanup()`` method is used at the end of every example. This is recommended to avoid leaving any pins on a high state after the end of your program.

IN Class examples
#################
This section contains examples on how to use GPIO pins as inputs.

Read a current GPIO value
*************************
In this example we create an instance of the ``libregpio.IN`` class and call the ``input`` method to read the pin value:


.. code-block:: python

       import libregpio as GPIO

       # set pin GPIOX_12 to be used as an input
       pin = GPIO.IN('GPIOX_12')

       # read pin value
       value = pin.input()

       # print read value
       print(value)

       GPIO.cleanup()

Pull up and Pull down resistors
*******************************
When using a pin as an input it may be at a floating state, sending unreliable values. To prevent this, the ``bias`` parameter can be used in the ``input`` method to set ``pull-up`` or ``pull-down`` resistors. 

This is the same example as above, but setting a pull-down bias:


.. code-block:: python

       import libregpio as GPIO

       # set pin GPIOX_12 to be used as an input
       pin = GPIO.IN('GPIOX_12')

       # read pin value with a pull-down resistor
       value = pin.input(bias='pull-down')

       # print read value
       print(value)

       GPIO.cleanup()

Wait for an edge event
**********************
In some applications you may want your program to wait for a falling-edge or rising-edge event. For this, you can use the ``wait_for_edge`` method.

In this example we are using a PIR motion sensor connected to the GPIOX_12 pin. The program waits for a rising-edge event before printing the corresponding value:


.. code-block:: python

       import libregpio as GPIO

       # set pin GPIOX_12 to be used as an input
       pin = GPIO.IN('GPIOX_12')

       # wait for a rising-edge event. Bias is set to pull-down
       value = pin.wait_for_edge(bias='pull-down', edge='rising')

       # print event value
       print(value)

       GPIO.cleanup()

.. note::
       You can use the ``num_events`` parameter if you want to wait for more than one event occurrence.


OUT Class examples
##################
In this section, we will turn an LED on for three seconds using the different methods of the ``libregpio.OUT`` class.

output method
*************
.. code-block:: python

       import libregpio as GPIO
       from time import sleep

       # set pin GPIOX_5 to be used as an output
       led = GPIO.OUT('GPIOX_5')

       # send a 1 value and return it to 0 after 3 seconds
       led.output(1)
       sleep(3)
       led.output(0)

       GPIO.cleanup()

high and low methods
********************
.. code-block:: python

       import libregpio as GPIO
       from time import sleep

       # set pin GPIOX_5 to be used as an output
       led = GPIO.OUT('GPIOX_5')

       # set the pin output to high and return to low after 3 seconds
       led.high()
       sleep(3)
       led.low()

       GPIO.cleanup()

toggle method
*************
.. code-block:: python

       import libregpio as GPIO
       from time import sleep

       # set pin GPIOX_5 to be used as an output
       led = GPIO.OUT('GPIOX_5')

       # set the pin output to high and return to low after 3 seconds
       led.toggle()
       sleep(3)
       led.toggle()

       GPIO.cleanup()

API documentation
=================

.. warning::
       Although this module contains a PWM class, it is not currently working properly. Be aware that using this class and its methods can lead to unexpected results.

.. automodule:: libregpio
   :members:
   :undoc-members:
   :show-inheritance:
