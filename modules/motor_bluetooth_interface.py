# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
from motor import Car
from bluedot import BlueDot
from signal import pause

# Car

class BtCarInterface:
    def __init__(self, car):
        self.bluetooth = BlueDot()
        self.bt_interface_code = 0
        self.bt_motor_interface()
        self.car = car

    def bt_motor_interface(self):
        if self.bt_interface_code == 1:
            self.bt_interface_code = 0
            for i in range(self.bluetooth.rows):
                for j in range(self.bluetooth.cols):
                    self.bluetooth[j, i].square = False
                    self.bluetooth[j, i].visible = False

            self.bluetooth.resize(1,1)
            self.bluetooth[0,0].square = False
            self.bluetooth[0,0].visible = True

        self.bluetooth.when_released = self.stop
        self.bluetooth.when_moved = self.slides
        self.bluetooth.when_double_pressed = self.swap_interface
        
    def bt_util_interface(self):
        self.bluetooth.resize(3, 3)

        for i in range(self.bluetooth.rows):
            if i == 0:
                color = (255, 255, 204) # day mode, with brighter music
            elif i == 1:
                color = (255, 0, 0)
            elif i == 2:
                color = (204, 204, 205) # night mode, with calm music

            for j in range(self.bluetooth.cols):
                self.bluetooth[j, i].square = True if i == 1 else False
                self.bluetooth[j, i].color = color

        # reset
        self.bluetooth.when_released = None
        self.bluetooth.when_moved = None
        self.bluetooth.when_double_pressed = None

        self.bluetooth[0, 1].visible = False
        self.bluetooth[2, 1].visible = False
        self.bluetooth[1, 1].color = "red"
        self.bluetooth[1, 1].when_double_pressed = self.swap_interface
        self.bt_interface_code = 1

    def swap_interface(self):
        if(self.bt_interface_code == 1):
            self.bt_motor_interface()
        else:
            self.bt_util_interface()

    def stop(self):
        print("stop")
        self.car.stop()

    def slides(self, pos):
        # speed
        duty_cycle = round(pos.distance * 100, 0)

        # direction
        tan = pos.y / pos.x
        if(-1 <= tan and tan <= 1) and (pos.x >= 0):
            print("clockwise: power {}%".format(duty_cycle))
            self.car.clockwise(duty_cycle = duty_cycle)
        elif(-1 >= tan or tan >= 1) and (pos.y >= 0):
            print("forward: power {}%".format(duty_cycle))
            self.car.forward(duty_cycle = duty_cycle)
        elif(-1 <= tan and tan <= 1) and (pos.x < 0):
            print("CounterClockwise: power {}%".format(duty_cycle))
            self.car.counterClockwise(duty_cycle = duty_cycle)
        elif(-1 >= tan or tan >= 1) and (pos.y <= 0):
            print("backward: power {}%".format(duty_cycle))
            self.car.backward(duty_cycle = duty_cycle)


if __name__ == "__main__":
    car = Car()
    interface = BtCarInterface(car)
    pause()
