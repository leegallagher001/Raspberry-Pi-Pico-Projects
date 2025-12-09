# Light Sensor Introduction - Raspberry Pi Pico H (MicroPython)
# A basic introduction to using a light sensor with the Pi Pico H with MicroPython
# Uses a photo transistor (light sensor) to take light readings
# each second and activate LEDs based on the reading
# Made with the instruction of Day 6 of the "12 Projects Of Codemas" by Pi Hut

from machine import ADC, Pin # imports pins and ADC for use
import time # imports the time module

# initialise LEDs and pin outputs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True: # continuous loop
    
    lightsensor = ADC(Pin(26)) # initialises light sensor for use with pin 26 in ADC mode

    light = lightsensor.read_u16() # stores light reading as 16-bit integer
    lightpercent = round(light/65535*100, 1) # stores light reading as percentage rounded to 1 decimal place

    print("Light Reading: " + str(light)) # prints the light reading as 16-bit integer
    print("Light Percentage: " + str(lightpercent) + "%") # prints light reading as percentage
    print("\n") # prints empty line for readability in shell
    
    time.sleep(1)
    
    if lightpercent <= 30: # light level less or equal to 30%
        
        red.value(1)
        amber.value(0)
        green.value(0)
        
    elif 30 < lightpercent < 60: # light level between 30-60%

        red.value(1)
        amber.value(1)
        green.value(0)
        
    elif lightpercent >= 60: # light level above 60%
        
        red.value(1)
        amber.value(1)
        green.value(1)