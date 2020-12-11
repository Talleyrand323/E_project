## motor.py ##

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
#from bluedot import BlueDot
import warnings

warnings.filterwarnings(action='ignore')

# GPIO Pins
leftWheelForward = 5 
leftWheelBackward = 6 
rightWheelForward = 13
rightWheelBackward = 19

# short moves
TICK = 0.025

class Car:
    def __init__(self, 
            LF = leftWheelForward, 
            LB = leftWheelBackward, 
            RF = rightWheelForward, 
            RB = rightWheelBackward):
        self.LF = LF
        self.LB = LB
        self.RF = RF
        self.RB = RB
        self.pwm_LF = None
        self.pwm_LB = None
        self.pwm_RF = None
        self.pwm_RB = None
    
    # basic movements
    def setup(self, hertz = 75):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LF, GPIO.OUT)
        GPIO.setup(self.RF, GPIO.OUT)
        GPIO.setup(self.LB, GPIO.OUT)
        GPIO.setup(self.RB, GPIO.OUT)
        self.pwm_LF = GPIO.PWM(self.LF, hertz) 
        self.pwm_LB = GPIO.PWM(self.LB, hertz) 
        self.pwm_RF = GPIO.PWM(self.RF, hertz) 
        self.pwm_RB = GPIO.PWM(self.RB, hertz) 
    
    def forward(self, t = TICK, duty_cycle = 50):
        self.setup()
        (self.pwm_LF).start(duty_cycle)
        (self.pwm_RF).start(duty_cycle)
        time.sleep(t)
        self.stop()

    def backward(self, t = TICK, duty_cycle = 50):
        self.setup()
        (self.pwm_LB).start(duty_cycle)
        (self.pwm_RB).start(duty_cycle)
        time.sleep(t)
        self.stop()

    def clockwise(self, t = TICK, duty_cycle = 50):
        self.setup()
        (self.pwm_LF).start(duty_cycle)
        (self.pwm_RB).start(duty_cycle)
        time.sleep(t)
        self.stop()

    def counterClockwise(self, t = TICK, duty_cycle = 50):
        self.setup()
        (self.pwm_LB).start(duty_cycle)
        (self.pwm_RF).start(duty_cycle)
        time.sleep(t)
        self.stop()

    def stop(self):
        (self.pwm_LF).stop()
        (self.pwm_LB).stop()
        (self.pwm_RF).stop()
        (self.pwm_RB).stop()
        GPIO.cleanup()


if __name__ == "__main__":
    # Car
    smartCar = Car()

    # initial moves
    smartCar.forward(1)
    smartCar.backward(1)
    smartCar.clockwise(1)
    smartCar.backward(1)
    smartCar.counterClockwise(1)
    smartCar.forward(1)
