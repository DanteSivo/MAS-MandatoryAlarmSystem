import time
from rpi_ws281x import *
import RPi.GPIO as GPIO
import math

LED_COUNT       = 200
LED_PIN         = 12
LED_FREQ_HZ     = 800000
LED_DMA         = 10
LED_BRIGHTNESS  = 25
LED_INVERT = False
LED_CHANNEL = 0

CONTROLLER_PIN = 26
RELAY_PIN = 33
BUTTON_PIN = 11


def clearStrip():
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def setStripRGB(R, G, B):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i , Color(R,G,B))
    strip.show()

if __name__ == '__main__':
    # Create NeoPixel object with parameters from top of file
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Initalize library
    strip.begin()

    GPIO.setmode (GPIO.BOARD)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    clearStrip()

    c = 0

    GPIO.output(RELAY_PIN,GPIO.LOW) # Enable RaspPi control

    while True:
        if (c < 255):
            c = c + 1
        else:
            c = 255
        
        if (GPIO.input(BUTTON_PIN) == GPIO.HIGH):
           c = 0
        print(GPIO.input(BUTTON_PIN))
        setStripRGB(c,c,math.floor(c/7))
        time.sleep(0.01)
