import RPi.GPIO as GPIO

pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
    print(GPIO.input(pin))
