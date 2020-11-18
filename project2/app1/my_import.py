import subprocess
import RPi.GPIO as GPIO
import time
import sys 

class Car(object):
	def __init__(self, LF, LB, RF, RB):
		self.LF = LF
		self.LB = LB
		self.RF = RF
		self.RB = RB
		
	def setup(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.LF, GPIO.OUT)
		GPIO.setup(self.RF, GPIO.OUT)
		GPIO.setup(self.LB, GPIO.OUT)
		GPIO.setup(self.RB, GPIO.OUT)
    
	def forward(self, t):
		self.setup()
		GPIO.output(self.LF, GPIO.HIGH)
		GPIO.output(self.RF, GPIO.HIGH)
		time.sleep(t)
		GPIO.output(self.LF, GPIO.LOW)
		GPIO.output(self.RF, GPIO.LOW)
		GPIO.cleanup()

	def backward(self, t):
		self.setup()
		GPIO.output(self.LB, GPIO.HIGH)
		GPIO.output(self.RB, GPIO.HIGH)
		time.sleep(t)  
		GPIO.output(self.LB, GPIO.LOW)
		GPIO.output(self.RB, GPIO.LOW)
		GPIO.cleanup()

	def clockwise(self, t):
		self.setup()
		GPIO.output(self.LF, GPIO.HIGH)
		GPIO.output(self.RB, GPIO.HIGH)
		time.sleep(t)  
		GPIO.output(self.LF, GPIO.LOW)
		GPIO.output(self.RB, GPIO.LOW)
		GPIO.cleanup()

	def counterClockwise(self, t):
		self.setup()
		GPIO.output(self.LB, GPIO.HIGH)
		GPIO.output(self.RF, GPIO.HIGH)
		time.sleep(t)  
		GPIO.output(self.LB, GPIO.LOW)
		GPIO.output(self.RF, GPIO.LOW)
		GPIO.cleanup()


#######################################################################3


class Servo(object):
	def __init__(self, UD, LR):
		self.UD = UD
		self.LR = LR
		self.UD_p = GPIO.PWM(UD,10)
		self.LR_p = GPIO.PWM(LR,10)

	def setup(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.UD, GPIO.OUT)
		GPIO.setup(self.LR, GPIO.OUT)

	def up(self):
		self.setup()
		self.UD_p.start(0)
		self.UD_p.ChangeDutyCycle(6.5) 
		time.sleep(0.000001)
		self.UD_p.stop()
		GPIO.cleanup()

	def down(self):
		self.setup()
		self.UD_p.start(0)
		self.UD_p.ChangeDutyCycle(6.5) 
		time.sleep(0.000001)
		self.UD_p.stop()
		GPIO.cleanup()

	def left(self):
		self.setup()
		self.LR_p.start(0)
		self.LR_p.ChangeDutyCycle(6.5) 
		time.sleep(0.000001)
		self.LR_p.stop()
		GPIO.cleanup()

	def right(self):
		self.setup()
		self.LR_p.start(0)
		self.LR_p.ChangeDutyCycle(6.5) 
		time.sleep(0.000001)
		self.LR_p.stop()
		GPIO.cleanup()
		






