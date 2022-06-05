import BlynkLib
import time
import RPi.GPIO as GPIO


BLYNK_AUTH = 'FGdf7HVxMrPLgGbWnOIF6LGgyh2meU3y'

blynk = BlynkLib.Blynk(BLYNK_AUTH)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN)


try:
    
    while True:
        
        blynk.run()
        if (GPIO.input(10)!=1):
            blynk.notify('Kapı Açıldı')
        elif (GPIO.input(10) == 1):
            blynk.notify('Kapı Kapandı')
   
finally:
    GPIO.cleanup()


