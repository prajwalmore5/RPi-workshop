import time, sys
import RPi.GPIO as GPIO

pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
def action(pin):
    print('Sensor detected action!')
    return
 
GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_callback(pin, action)
 
try:
    while True:
        print('alive')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
