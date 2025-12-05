# Onboard LED - Raspberry Pi Pico H (MicroPython)
# A basic introduction to the Pi Pico's onboard LED control with MicroPython
# Made with the instruction of Day 1 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin # imports GPIO pin usage

print("Basic LED program")

onboardLED = Pin(25, Pin.OUT) # initialises Pin 25 (the on-board LED) for output
onboardLED.value(1) # changes value of pin 25 to 1 (LED On)