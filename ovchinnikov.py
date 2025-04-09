import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3 ,4 ,17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)
# for i in range(3):
#     for j in leds:
#         GPIO.output(j,1)
#         time.sleep(0.2)
#         GPIO.output(j,0)
# GPIO.output(leds,0)
# GPIO.cleanup()
# dac = [8,11,7,1,0,5,12,6]
# GPIO.setup(dac, GPIO.OUT)
# number = [0,1,0,0,0,0,0,0]
# GPIO.output(dac,number)
# time.sleep(20)
# GPIO.output(dac,[0]*8)
# GPIO.cleanup
aux = [21,20,26,16,19,25,23,24]
GPIO.setup(aux,GPIO.IN)
while True:
    for i in leds:
        GPIO.output(i, GPIO.input(aux[leds.index(i)]))
GPIO.output(leds, 0)
GPIO.cleanup()