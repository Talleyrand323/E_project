
#############################          Imports         ###########################
from __future__ import unicode_literals

from django.template import loader
from django.utils import timezone
import numpy as np
import threading
from django.http import StreamingHttpResponse
from datetime import datetime
import os
import cv2

#from app.models import Image

directory = os.getcwd()
filePath = directory + '/app/templates/resources/images/'

######################################
from django.shortcuts import render
from django.http import HttpResponse

import subprocess
import RPi.GPIO as GPIO
import time
import sys 

#############################          Navigate         ###########################

def home(request):
    
    return render(request, 'home.html')


def main(request):
    
    return render(request, 'main.html')

def main2(request):
    
    return render(request, 'main2.html')

#############################          Servos         ###########################
pin =18 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
#p= GPIO.PWM(pin, 10)
GPIO.setwarnings(False)

def left(request):
	p.start(0)
	p.ChangeDutyCycle(6.5) 
	time.sleep(0.000001)
	p.stop()
	return render(request, 'main.html')

def right(request):
	p.start(30)
	p.ChangeDutyCycle(1.5) 
	#bot(18).servo_speed(-75)
	time.sleep(0.000001)
	p.stop()
	return render(request, 'main.html')
 



#############################          Camera         ###########################

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		(self.grabbed, self.frame) = self.video.read()
		threading.Thread(target=self.update, args=()).start()

	def __del__(self):
		self.video.release()

	def get_frame(self):
		image = self.frame
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()		

	def update(self):
		while True:
			(self.grabbed, self.frame) = self.video.read()

	def take_frame(self):
		now = datetime.now()
		fileName = filePath + now.strftime('%y%m%d_%H%M%S') + '.png'
		print (fileName)
		cv2.imwrite(fileName, self.frame)

		db = Image(image_name=now.strftime('%y%m%d_%H%M%S'), pub_date=timezone.now())
		db.save()


cam = VideoCamera()

def gen(camera):
	while True:
		frame = cam.get_frame()
		yield(b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def stream(request):
    try:
        return StreamingHttpResponse(gen(()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass






#############################          Wheels         ###########################

class Car:
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

# GPIO Pins
LF = 5 
LB = 6 
RF = 13
RB = 19

# Car
smartCar = Car(LF, LB, RF, RB)


smartCar.forward(0.25)
smartCar.backward(0.25)
smartCar.clockwise(0.25)
smartCar.counterClockwise(0.5)


#GPIO.cleanup()





