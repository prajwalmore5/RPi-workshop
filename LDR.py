
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin = 7


def rc_time (pin):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1
        
    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
