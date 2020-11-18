# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

leftWheelForward = 5 
leftWheelBackward = 6 
rightWheelForward = 13
rightWheelBackward = 19

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
#        GPIO.cleanup()

    def backward(self, t):
        self.setup()
        GPIO.output(self.LB, GPIO.HIGH)
        GPIO.output(self.RB, GPIO.HIGH)
        time.sleep(t)  
        GPIO.output(self.LB, GPIO.LOW)
        GPIO.output(self.RB, GPIO.LOW)
 #       GPIO.cleanup()

    def clockwise(self, t):
        self.setup()
        GPIO.output(self.LF, GPIO.HIGH)
        GPIO.output(self.RB, GPIO.HIGH)
        time.sleep(t)  
        GPIO.output(self.LF, GPIO.LOW)
        GPIO.output(self.RB, GPIO.LOW)
  #      GPIO.cleanup()

    def counterClockwise(self, t):
        self.setup()
        GPIO.output(self.LB, GPIO.HIGH)
        GPIO.output(self.RF, GPIO.HIGH)
        time.sleep(t)  
        GPIO.output(self.LB, GPIO.LOW)
        GPIO.output(self.RF, GPIO.LOW)
   #     GPIO.cleanup()

# GPIO Pins
leftWheelForward = 5 
leftWheelBackward = 6 
rightWheelForward = 13
rightWheelBackward = 19

# Car
smartCar = Car(leftWheelForward, leftWheelBackward, rightWheelForward, rightWheelBackward)
smartCar.forward(0.25)
smartCar.backward(0.25)
smartCar.clockwise(0.25)
smartCar.counterClockwise(1)



