# Basic Functions & Jingle Bells - Raspberry Pi Pico H (MicroPython)
# A basic introduction to using functions with the Pi Pico H with MicroPython
# Uses a function to feed various notes into a buzzer program, creating a shortened "Jingle Bells" tune, utilising PWM
# Volume control is also included with the potentiometer, but
# for this program it can't be changed whilst the tune is playing, only set beforehand
# Made with the instruction of Day 5 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin, PWM, ADC
import time

buzzer = PWM(Pin(13)) # initialises buzzer on pin 13 with PWM mode
potentiometer = ADC(Pin(27)) # initialises potentiometer on pin 27 with ADC

# A 'library' of frequencies (tones) we'll be using for the song
C = 523
D = 587
E = 659
G = 784

volume = potentiometer.read_u16() # volume (for duty cycle)

def playtone(note,vol,delay1,delay2): # our function
    buzzer.duty_u16(vol) # sets volume
    buzzer.freq(note) # plays a note at one of the frequencies in the library
    time.sleep(delay1) # plays for "delay1" time
    buzzer.duty_u16(0) # stops playing note
    time.sleep(delay2) # stops for "delay2" time
    
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.5) # longer delay for third note

playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.5) # longer delay for third note

playtone(E,volume,0.1,0.2)
playtone(G,volume,0.1,0.2)
playtone(C,volume,0.1,0.2)
playtone(D,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)

buzzer.duty_u16(0) # duty cycle to 0 to turn buzzer off