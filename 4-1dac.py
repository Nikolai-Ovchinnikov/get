import RPi.GPIO as GPIO
DAC = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)
def dvoich(a):
    k = []
    while a!=0:
        k.append(a%2)
        a = a//2
    k = k[::-1]
    if len(k)<8:
        k = [0]*(8-len(k))+k
    return k
try:
    while True:
        try:
            print('Введите целое число от 0 до 255 включительно')
            chislo = input()
            res=int(chislo)
            if res>255:
                print('Введите число меньше 255.')
            if res<0:
                print('Введите число больше 0.')
            if res<256 and res>0:
                GPIO.output(DAC,dvoich(res))
                print(3.3*res/256)
        except ValueError:
            if chislo=='q':
                break
            try:
                aa = float(chislo)
                print('Введите целое число, а не нецелое число.')
            except ValueError:
                print('Введите целое число, а не строку или символ.')
                continue
            finally:
                dd =1
            continue  
        finally:
            aa=1
finally:
    GPIO.output(DAC,0)
    GPIO.cleanup()