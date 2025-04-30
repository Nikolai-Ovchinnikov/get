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
def adc():
    a = 0
    GPIO.output(dac,dectobin(128))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com == 0:
        a+=128
    GPIO.output(dac,dectobin(64+a))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=64
    GPIO.output(dac,dectobin(32+a))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=32
    GPIO.output(dac,dectobin(16+a))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=16
    GPIO.output(dectobin(8+a),dac)
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=8
    GPIO.output(dac,dectobin(4+a))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=4
    GPIO.output(dac,dectobin(2+a))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=2
    GPIO.output(dac,dectobin(1+a))
    time.sleep(0.001)
    com = GPIO.input(comp)
    if com==0:
        a+=1
    print(a,a*3.3/256)
try:
    while(True):
        adc()
finally:
    GPIO.output(dac,[0]*8)
    GPIO.cleanup()      