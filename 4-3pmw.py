import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
pmw = GPIO.PWM(23, 100)
pmw.start(0)
try:
    while True:
        k = float(input())
        pmw.ChangeDutyCycle(k)            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
