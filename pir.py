import RPi.GPIO as GPIO #Import GPIO library
import time #Import time library 

GPIO.setmode(GPIO.BOARD) #Set GPIO pin numbering 

pir = 40 #Associate pin 26 to pir 

GPIO.setup(pir, GPIO.IN) #Set pin as GPIO in print "Waiting for sensor to settle" 

time.sleep(2) #Waiting 2 seconds for the sensor to initiate print "Detecting motion" 

while True: 

    if GPIO.input(pir): #Check whether pir is HIGH print "Motion Detected!"
        print("enemy spotted ")

        time.sleep(2) #D1- Delay to avoid multiple detection
    else:
        print("clear")

    time.sleep(0.1) #While loop delay should be less than detection(hardware) delay
