import RPi.GPIO as GPIO
import time

pin =17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p= GPIO.PWM(pin, 50)  #PMW:펄스 폭 변조
p.start(0)
cnt = 0

try:

	while True:
		p.ChangeDutyCycle(12.5) #최댓값
		time.sleep(2)
		p.ChangeDutyCycle(10.0)
		time.sleep(2)
		p.ChangeDutyCycle(7.5) #0
		time.sleep(2)
		p.ChangeDutyCycle(5.0)
		time.sleep(2)
		p.ChangeDutyCycle(2.5) #최솟값
		time.sleep(2)

except KeybordInterrupt:
	p.stop()    

GPIO.cleanup()

