import RPi.GPIO as GPIO
import time

ledPin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
while True:
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(10)
