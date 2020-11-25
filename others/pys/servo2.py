from time import sleep
import RPi.GPIO as GPIO
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global panServoAngle
global tiltServoAngle
panServoAngle = 90
tiltServoAngle = 90

panPin = 27
tiltPin = 17


def setServoAngle(servo, angle):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo, GPIO.OUT)
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()
	GPIO.cleanup()
    
def moveServo(servo, angle):
	global panServoAngle
	global tiltServoAngle
	warning = ''
	if servo == 27:
		if angle == 1:
			panServoAngle = panServoAngle + 10
			
		else:
			panServoAngle = panServoAngle - 10


		setServoAngle(27, panServoAngle)

	elif servo == 17:
		if angle == 1:
			tiltServoAngle = tiltServoAngle + 10
			print(tiltServoAngle)
		else:
			tiltServoAngle = tiltServoAngle - 10
			print(tiltServoAngle)	

		setServoAngle(17, tiltServoAngle)
		
moveServo(17, 1)

sleep(1)

moveServo(17, 1)

sleep(1)

moveServo(17, 1)

sleep(1)

moveServo(17, 0)

sleep(1)

moveServo(17, 0)

sleep(1)



