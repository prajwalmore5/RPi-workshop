import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))

# main() function
def main():
    # use sys.argv if needed
    '''if len(sys.argv) < 2:
        print('Usage: python tstest.py PRIVATE_KEY')
        #exit(0)'''
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=6EREBHKYCAYQJU6B'
    
    while True:
        try:
            RH, T = getSensorData()
            #f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T))
            f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T)) 
            #f = urllib2.urlopen("https://api.thingspeak.com/update?api_key=6EREBHKYCAYQJU6B&field1=0" % RH)
            print f.read()
            f.close()
            sleep(3)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()
