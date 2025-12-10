# Motion Sensor Introduction - Raspberry Pi Pico H (MicroPython)
# A basic introduction to using a PIR (passive infrared) motion sensor with the Pi Pico H with MicroPython
# Uses a PIR to detect motion nearby and sound an "alarm" (buzzer and LED lights) when motion is detected
# Made with the instruction of Day 7 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin, PWM
import time

# initialise LEDs and pins for output
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin. OUT)

# initialise buzzer on pin 13 in PWM mode
buzzer = PWM(Pin(13))

# set duty cycle to 0 at start
buzzer.duty_u16(0)

pir = Pin(26, Pin.IN, Pin.PULL_DOWN) # initialises PIR sensor on pin 26 for input and pullds power down to LOW

print("Motion Sensor: Loading...")

time.sleep(10) # this delay allows the sensor to calibrate itself properly

print("Motion Sensor: Ready!")

def motion_alarm(): # buzzer alarm function
    
    buzzer.duty_u16(10000)
    
    for i in range(5): # run 5 times
        
        buzzer.freq(5000) # high pitch
        
        #LEDs on
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(1) # lights on and high pitch for 1 second
        
        buzzer.freq(500) # low pitch
        
        # LEDs off
        red.value(0)
        amber.value(0)
        green.value(0)
        
        time.sleep(1) # lights off and low pitch for 1 second
        
    buzzer.duty_u16(0) # switch buzzer off once function has ran

while True: # continuous loop
    
    time.sleep(0.01) # short delay
    
    if pir.value() == 1: # if sensor detects movement
        
        print("Movement Detected!")
        
        motion_alarm() # activate alarm function
        
        print("Sensor Scanning")