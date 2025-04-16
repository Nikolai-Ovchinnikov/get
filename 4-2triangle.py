import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(a):
    k = []
    while a!=0:
        k.append(a%2)
        a = a//2
    k = k[::-1]
    if len(k)<8:
        k = [0]*(8-len(k))+k
    return k
print('Введите число - период.')
period = input()
try:
    res = int(period)
except ValueError:
    print('период это число а не символ!')

try:
    t = 1
    shag = 1
    while True:
        GPIO.output(dac, dec2bin(t))
        if t==255 or t==0:
            shag = -1
        time.sleep(res/512)
        t+=shag

finally:
    GPIO.output(dac, 0)