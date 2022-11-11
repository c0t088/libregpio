Importing the module
====================

To import the libregpio module:

.. code-block::

       import libregpio as GPIO
       
This way allows you to refer to it as GPIO for the rest of your program.

PIN Reference
=============
To access the 40-pin GPIO via *gpiod* is required to use the Linux pin number. The libregpio module uses a dictionary, so the pins are initialized by its Name when creating an class object.

.. code-block::

       import libregpio as GPIO

        a_pin = GPIO.IN('GPIOX_4')
       
Please, see Libre Computer's GPIO Headers Reference: https://docs.google.com/spreadsheets/d/1U3z0Gb8HUEfCIMkvqzmhMpJfzRqjPXq7mFLC-hvbKlE/edit#gid=0

API documentation
=================

.. automodule:: libregpio
   :members:
   :undoc-members:
   :show-inheritance:
