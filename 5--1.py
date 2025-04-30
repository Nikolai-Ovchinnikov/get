import RPi.GPIO as GPIO
import time 
dac = [8, 11, 7, 1, 0, 5, 12, 6]

comp = 14
troyka = 13

GPIO.setmode( GPIO.BCM )

GPIO.setup( dac, GPIO.OUT )
GPIO.setup( troyka, GPIO.OUT, initial =1)
GPIO.setup( comp, GPIO.IN )
def dectobin(x):
    if x==0:
        return [0]*8
    else:
        a = ''
        while x!=0:
            a+=str(x%2)
            x = x//2
        res = []
        for j in range(1,len(a)+1):
            res.append(int(a[-j]))
        if len(res)<8:
            res = [0]*(8-len(res))+res
        return res
def adc(k):
    for i in range(256):
        ch = dectobin(i)
        GPIO.output(k,ch)
        time.sleep(0.05)
        com = GPIO.input(comp)
        if com == 1:
            print(i,i*3.3/256)
            break
try:
    while(True):
        adc(dac)
finally:
    GPIO.output(dac,[0]*8)
    GPIO.cleanup()       