import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#set PIR motion sensor on 11th pin
GPIO.setup(11, GPIO.IN)
while True:
    i=GPIO.input(11)
    # sensor not detecting anything
    if i==0:
        print("No intruders",i)
        time.sleep(1)
    # sensor triggered
    elif i==1:
        print("Intruder detected",i)
    time.sleep(1)