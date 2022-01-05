import time
from rpi_ws281x import *
import RPi.GPIO as GPIO
import math
import random
from datetime import datetime, timedelta, tzinfo

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

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(hours=offset)
        self.__dst = timedelta(hours=offset-1)
        self.__name = ''

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return self.__dst

# Dictonary of standard timezones. Offset to GMT
timezone_dict = {
    "PST": -8 ,
    "MST": -7 ,
    "CST": -6,
    "EST": -5,
    "GMT": 0,
    "CST": 8,
    "JST": 9,
    "AEDT": 11,
    "NZDT": 13
}


''' get_current_time
Description : Helper function to get current time based on timezone initals
                or fixed offset value
'''
def get_current_time(timezone = 'NA', offset = 24):
    if (offset != 24):  # If numerical offset was specified
        return datetime.now(FixedOffset(offset))
    elif timezone in timezone_dict: # Otherwise, check for timezone value
        return timezone_dict.value(timezone)
    else:
        return datetime.now() # If no parameters given. Get system timezone

def clearStrip():
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def use_tolerance(C, tolerance):
    output = C + tolerance
    if (output > 255):
        return 255
    elif (output < 0):
        return 0
    elif (output < 40):
        return C
    else:
        return output


def setStripRGB(colorArray):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, colorArray[i])
    strip.show()

def shift_right(list, num):
    output_list = []

    for item in range(len(list) - num, len(list)):
        output_list.append(list[item])

    for item in range(0, len(list) - num):
        output_list.append(list[item])

    return output_list

if __name__ == '__main__':
    # Create NeoPixel object with parameters from top of file
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Initalize library
    strip.begin()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    clearStrip()

    c = 0

    GPIO.output(RELAY_PIN,GPIO.LOW) # Enable RaspPi control

    R = 240
    G = 240
    B = 50

    tL = -20
    tH = 20

    delay = 0.26

    colors = [Color(0,0,0)] * LED_COUNT
    pulse_width = 4

    clearStrip()

    alarmHour = 21
    alarmMinute = 10

    alarmTime = datetime.now()
    alarmTime = alarmTime.replace(hour = alarmHour, minute = alarmMinute)

    while True: # System Loop
        # Only disable LED loop if alarm is current
        time.sleep(1)
        
        print("D" + str(datetime.now(FixedOffset(-5)).hour) + ":" + str(datetime.now(FixedOffset(-5)).minute))
        print("A" + str(alarmTime.hour) + ":" + str(alarmTime.minute))
        
        if (datetime.now().hour == alarmTime.hour and datetime.now().minute == alarmTime.minute):
            while True: # LED loop
                cR = R - random.randint(tL,tH)
                cG = G - random.randint(tL,tH)
                cB = B - random.randint(tL,tH)
                if (cR > 255):
                    cR = 255
                elif (cR < 0):
                    cR = abs(cR)

                if (cG > 255):
                    cG = 255
                elif (cG < 0):
                    cG = abs(cG)

                if (cB > 255):
                    cB = 255
                elif (cB < 0):
                    cB = abs(cB)

                print (str(cR) + ":" + str(cG) + ":" + str(cB))
                colors = shift_right(colors, pulse_width)
                for i in range(0, pulse_width):
                    colors[i] = Color(cR, cG, cB)
               
                setStripRGB(colors)
                time.sleep(delay)
