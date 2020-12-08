import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RED = 13

GREEN = 19

BLUE = 26

GPIO.setup(RED,GPIO.OUT)

GPIO.output(RED,0)

GPIO.setup(GREEN,GPIO.OUT)

GPIO.output(GREEN,0)

GPIO.setup(BLUE,GPIO.OUT)

GPIO.output(BLUE,0)

try:
	while (True):
		GPIO.output(RED, True)
		GPIO.output(GREEN, True)
		GPIO.output(BLUE, True)
except KeyboardInterrupt:
	GPIO.cleanup()


