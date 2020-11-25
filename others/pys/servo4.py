import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#6 and 0.072 to right, 8 and 0.1 to left

pin =17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p= GPIO.PWM(pin, 50)  #PMW:펄스 폭 변조
p.start(6)
time.sleep(0.072)
p.stop()

GPIO.cleanup()

