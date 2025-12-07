# Basic Analogue I/O - Raspberry Pi Pico H (MicroPython)
# A basic introduction to analogue control with the Pi Pico H with MicroPython
# Covers the basics of analogue I/O using a potentiometer and LEDs
# Made with the instruction of Day 4 of the "12 Projects Of Codemas" by Pi Hut

from machine import ADC, Pin # imports pins, ADC pins for use
import time # imports time module

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

reading = 0 # sets up a "reading" variable

potentiometer = ADC(Pin(27)) # sets up the potentiometer to use ADC pin 27

while True: # continuous loop
    
    reading = potentiometer.read_u16() # read the potentiometer value (16-bit output)
    print(reading) # print reading to shell
    time.sleep(0.1) # short delay
    
    if reading <= 20000:
        
        red.value(1)
        amber.value(0)
        green.value(0)
        
    elif 20000 < reading < 40000:
        
        red.value(1)
        amber.value(1)
        green.value(0)
        
    elif reading >= 40000:
        
        red.value(1)
        amber.value(1)
        green.value(1)
        

        
    
    