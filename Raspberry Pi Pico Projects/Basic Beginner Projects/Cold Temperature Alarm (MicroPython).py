# Cold Temperature Alarm - Raspberry Pi Pico H (MicroPython)
# Another introduction to using a 1-wire temperature sensor with the Pi Pico H with MicroPython
# Use of temperature sensor with buzzer to create a "temperature alarm" when it gets very cold (below 15°C)
# Unless the temperature change is very pronounced, the probe can take a little while to get an accurate reading
# Made with the instruction of Day 8 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin, PWM
import onewire, ds18x20, time # allows use of onewire devices and DS18B20 sensor

# initialise LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# buzzer setup
buzzer = PWM(Pin(13))
buzzer.duty_u16(0)

SensorPin = Pin(26, Pin.IN) # initialise pin 26 for input with temperature sensor

sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin)) # tells Pico which type of sensor is being used and on which pin

roms = sensor.scan() # scans for unique rom code of DS18B20

def cold_alarm(): # function to trigger alarm if temperature is colder than 15°C
    
    buzzer.duty_u16(10000) # volume up
    
    for i in range(5):
        
        buzzer.freq(5000) # high pitch
        
        # LEDs on
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(1) # high pitch and lights for 1 second
        
        buzzer.freq(1000) # low pitch
        
        #LEDs off
        red.value(0)
        amber.value(0)
        green.value(0)
        
        time.sleep(1) # low pitch and lights off for 1 second
        
    buzzer.duty_u16(0) # switch buzzer off at end of function

while True: # continuous loop
    
    time.sleep(5) # gives the sensor a couple of seconds to calibrate properly - needs at least 1 second
    
    for rom in roms: # only one sensor being used here, but this could allow use of multiple
        
        sensor.convert_temp() # convert sensor units to °C
        time.sleep(1) # always need to wait at least 1 second after converting
        
        temperature = sensor.read_temp(rom) # prints temperature in °C
        
        print("Temperature: " + str(temperature) + "°C")
        
        if temperature <= 15: # if less than 15°C
            
            cold_alarm() # calls the cold temperature alarm
        
        elif 15 < temperature < 18: # if 15-18°C
            
            red.value(0) 
            amber.value(0)
            green.value(1) # green ON - cold
            
        elif 18 < temperature < 25: # if 18-25°C
            
            red.value(0)
            amber.value(1)
            green.value(1) # green + amber ON - getting warmer
            
        elif temperature >= 25: # if above 25°C
            
            red.value(1)
            amber.value(1)
            green.value(1) # red + amber + green ON - HOT!