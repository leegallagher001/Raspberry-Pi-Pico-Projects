# Tilt Sensor - Raspberry Pi Pico H (MicroPython)
# An introduction to using a tilt sensor with the Pi Pico H with MicroPython
# This projects makes a "tilt alarm" and tilt counter using the buzzer and tilt sensor
# Tilt sensors useful for robotics projects, where a tilt sensor could act as a failsafe
# should the robot fall over
# Made with the instruction of Day 9 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin, PWM
import time

# Tilt Sensor setup, pin set up for input and power LOW
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Buzzer setup with PWM mode and frequency
buzzer = PWM(Pin(13))
buzzer.freq(1000)

# set up counter and state variables
tiltcounter = 0
state = 0

while True: # continuous loop
    
    time.sleep(0.01) # short delay
    
    if state == 0 and tilt.value() == 1: # if sensor power is HIGH (tilt detected)
        
        print("***TILT DETECTED***") # alert tilt detected
        
        state = 1 # activate state
        
        buzzer.duty_u16(10000) # volume up
        
        time.sleep(0.5) # buzzes for half a second
        
        buzzer.duty_u16(0) # volume down
        
        tiltcounter += 1 # add 1 to tilt count
        
        print("Tilts Counted: " + str(tiltcounter))
        
    if state == 1 and tilt.value() == 0: # if sensor is righted
        
        state = 0
        
        print("Sensor Righted!")
        print("\n")
        
        
        