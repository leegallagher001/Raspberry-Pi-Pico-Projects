# Basic External LED - Raspberry Pi Pico H (MicroPython)
# A basic introduction to controlling external LEDs using the Pi Pico H with MicroPython
# making a blinking traffic light pattern
# Made with the instruction of Day 2 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin # imports pins for use
import time # imports time module

red = Pin(18, Pin.OUT) # initialises pin 18 for output
amber = Pin(19, Pin.OUT) # initialises pin 19 for output
green = Pin(20, Pin.OUT) # initialises pin 20 for output

counter = 1 # declares "counter" with value of 1

while counter <= 10: # while counter is less than or equal to 10
    
    print("The counter is currently at: ", counter) # prints current count to shell
    
    # Red LED On
    red.value(1) # turns red LED on
    amber.value(0) # amber LED off
    green.value(0) # green LED off

    time.sleep(0.5) # waits 0.5 seconds

    # Amber LED On
    red.value(0) # red LED off
    amber.value(1) # turns amber LED on
    green.value(0) # green LED off
    
    time.sleep(0.5) # wait 0.5 seconds
    
    # Green LED On
    red.value(0) # red off
    amber.value(0) # amber off
    green.value(1) # turns green LED on
    
    time.sleep(0.5) # wait 0.5 seconds
    
    counter += 1 # increment counter by 1
    
# turns all LEDs off at end of loop
red.value(0)
amber.value(0)
green.value(0)
