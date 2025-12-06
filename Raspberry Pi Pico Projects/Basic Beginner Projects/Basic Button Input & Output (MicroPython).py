# Basic Button I/O - Raspberry Pi Pico H (MicroPython)
# A basic introduction to using buttons with the Pi Pico H with MicroPython
# Covers the basics of button input and LED output demonstrating various ways to control
# LEDs using the three buttons
# Made with the instruction of Day 3 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin # imports pins for use
import time # imports time module

# button set-up
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN) # (13 = pin, Pin.IN = initialised for input, Pin.PULL_DOWN = power pulled down to 0)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# LED setup
red = Pin(18, Pin.OUT) # initialises pin 18 for output to Red LED
amber = Pin(19, Pin.OUT) # initialises pin 19 for output to Amber LED
green = Pin(20, Pin.OUT) # initialises pin 20 for output to Green LED

while True: # sets up continuous loop
    
    time.sleep(0.5) # wait half a second
    
    if button1.value() == 1: # if button 1 is pressed
    # this uses the button input to turn an LED on/off using the value of 1 or 0
        
        print("Button 1 has been pressed!")
        
        if green.value() == 0: # if green light OFF
            green.value(1) # green ON
            amber.value(0) # amber OFF
            red.value(0) # red OFF
        else: # if green light ON
            green.value(0) # green OFF
        
    if button2.value() == 1: # if button 2 pressed
    # this button controls both the amber and red LEDs
        
        print("Button 2 has been pressed!")
        
        if amber.value() == 0 and red.value() == 0: # if both amber and red lights are OFF
            green.value(0) # green OFF
            amber.value(1) # amber ON
            red.value(1) # red ON
        else:
            amber.value(0) # amber OFF
            red.value(0) # red OFF
        
    if button3.value() == 1: # if button 3 pressed
    # this buttons uses the "toggle" function, to turn LEDs on if off, or off if on
    # effectively working as a switch
        
        print("Button 3 has been pressed!")
        green.toggle()
        amber.toggle()
        red.toggle()
        
    else: # if no buttons pressed
        
        print("No button presses detected")