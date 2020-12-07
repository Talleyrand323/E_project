# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
from bluedot import BlueDot
from signal import pause

GPIO.setwarnings(False)
GPIO.cleanup()

global pwm_L
global pwm_R
pwm_L = 70
pwm_R = 70


# bluedot setups
bd = BlueDot(cols = 3, rows = 5)
bd[0,0].visible = False
bd[2,0].visible = False

bd[1,1].visible = False

bd[0,2].visible = False
bd[2,2].visible = False

bd[0,3].visible = False
bd[1,3].visible = False
bd[2,3].visible = False

#bd[0,3].visible = False
#bd[1,3].visible = False
#bd[2,3].visible = False

leftWheelForward = 5
leftWheelBackward = 6
rightWheelForward = 13
rightWheelBackward = 19

class Car:
    global pwm_L
    global pwm_R

    def __init__(self, LF, LB, RF, RB):
        self.LF = LF
        self.LB = LB
        self.RF = RF
        self.RB = RB
        self.pwm_LF = pwm_L
        self.pwm_LB = pwm_L
        self.pwm_RF = pwm_R
        self.pwm_RB = pwm_R

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LF, GPIO.OUT)
        GPIO.setup(self.RF, GPIO.OUT)
        GPIO.setup(self.LB, GPIO.OUT)
        GPIO.setup(self.RB, GPIO.OUT)
        self.pwm_LF = GPIO.PWM(self.LF, pwm_L)
        self.pwm_LB = GPIO.PWM(self.LB, pwm_L)
        self.pwm_RF = GPIO.PWM(self.RF, pwm_R)
        self.pwm_RB = GPIO.PWM(self.RB, pwm_R)



    def swiped(self, swipe):
        print("Swiped")
        print("speed={}".format(swipe.speed))
        print("angle={}".format(swipe.angle))
        print("distance={}".format(swipe.distance))

    def move(self, pos):
        t = 0.1
        if pos.top:
            print("forward")
            #self.forward(t)
        elif pos.bottom:
            print("backward")
            #self.backward(t)
        elif pos.left:
            print("counterClockwise")
            #self.counterClockwise(t)
        elif pos.right:
            print("clockwise")
            #self.clockwise(t)

    def stop(self):
        (self.pwm_LF).stop()
        (self.pwm_RF).stop()
        (self.pwm_LB).stop()
        (self.pwm_RB).stop()
        GPIO.cleanup()


    def forward(self):
        self.setup()
        (self.pwm_LF).start(pwm_L)
        (self.pwm_RF).start(pwm_R)
        time.sleep(t)
        (self.pwm_LF).stop()
        (self.pwm_RF).stop()
        GPIO.cleanup()

    def backward(self):
        self.setup()
        (self.pwm_LB).start(pwm_L)
        (self.pwm_RB).start(pwm_R)

    def clockwise(self):
        self.setup()
        (self.pwm_LF).start(pwm_L)
        (self.pwm_RB).start(pwm_R)

    def counterClockwise(self):
        self.setup()
        (self.pwm_LB).start(pwm_L)
        (self.pwm_RF).start(pwm_R)


    '''
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
'''
# GPIO Pins
leftWheelForward = 5
leftWheelBackward = 6
rightWheelForward = 13
rightWheelBackward = 19

# Car
smartCar = Car(leftWheelForward, leftWheelBackward, rightWheelForward, rightWheelBackward)

# initial moves
#bd.when_pressed = smartCar.move
#bd.when_moved = smartCar.move
bd.when_released = smartCar.stop
bd.when_swiped = smartCar.swiped

pause()

