# Buzzer & Volume Control - Raspberry Pi Pico H (MicroPython)
# A basic introduction to using a buzzer with the Pi Pico H with MicroPython
# Sets up a buzzer with a potentiometer for volume control, utilising PWM and ADC
# Made with the instruction of Day 5 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin, PWM, ADC
import time

potentiometer = ADC(Pin(27)) # initialises potentiometer on ADC mode with pin 27
buzzer = PWM(Pin(13)) # initialises buzzer on PWM mode with pin 13

reading = 0 # reading of potentiometer value, initial value 0

while True: # continuous loop
    
    time.sleep(0.01) # short delay
    
    reading = potentiometer.read_u16() # reads the potentiometer value as a 16-bit integer
    
    buzzer.freq(500) # frequency (sets tone)
    buzzer.duty_u16(reading) # uses reading to set duty cycle (sets volume)
    
    print(reading) # print current reading to shell