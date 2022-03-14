import RPi.GPIO as GPIO

b = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(b) == GPIO.HIGH:
        print("Button was pushed")
    else:
        print("L")
