# Basic PWM - Raspberry Pi Pico H (MicroPython)
# A basic introduction to Pulse Width Modulation (PWM) with the Pi Pico H with MicroPython
# Covers the basics of PWM and duty cycles using a potentiometer to vary the brightness of an LED
# Made with the instruction of Day 4 of the "12 Projects Of Codemas" by Pi Hut

from machine import ADC, Pin, PWM # imports pins, ADC pins and PWM for use
import time # imports time module

led = PWM(Pin(18)) # sets up pin 18 for PWM with LED

led.freq(1000) # sets PWM frequency (how often power switches between ON and OFF)

reading = 0 # sets up a "reading" variable

potentiometer = ADC(Pin(27)) # sets up the potentiometer to use ADC pin 27

while True: # continuous loop
    
    reading = potentiometer.read_u16() # read the potentiometer value (16-bit output)
    print(reading) # print reading to shell
    
    led.duty_u16(reading) # sets duty cycle to potentiometer value
    
    time.sleep(0.01) # short delay - reading in shell struggles to keep up at 0.001 or 0.002
    
    