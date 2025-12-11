# Temperature Sensor Intro - Raspberry Pi Pico H (MicroPython)
# An introduction to using a 1-wire temperature sensor with the Pi Pico H with MicroPython
# Simple use of temperature sensor with LEDs to indicate if it is cold, warm or hot (well, warmer)
# The probe takes a little while to get an accurate fix on the temperature, so any changes to the
# reading tend to be quite slow I found
# Made with the instruction of Day 8 of the "12 Projects Of Codemas" by Pi Hut

from machine import Pin
import onewire, ds18x20, time # allows use of onewire devices and DS18B20 sensor

# initialise LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

SensorPin = Pin(26, Pin.IN) # initialise pin 26 for input with temperature sensor

sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin)) # tells Pico which type of sensor is being used and on which pin

roms = sensor.scan() # scans for unique rom code of DS18B20

while True: # continuous loop
    
    time.sleep(5) # gives the sensor a couple of seconds to calibrate properly - needs at least 1 second
    
    for rom in roms: # only one sensor being used here, but this could allow use of multiple
        
        sensor.convert_temp() # convert sensor units to °C
        time.sleep(1) # always need to wait at least 1 second after converting
        
        temperature = sensor.read_temp(rom) # prints temperature in °C
        
        print("Temperature: " + str(temperature) + "°C")
        
        if temperature <= 18: # if less than 18°C
            
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
        
        