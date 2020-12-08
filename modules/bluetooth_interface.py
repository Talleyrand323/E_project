# Import required libraries
import sys
import time
import threading
import RPi.GPIO as GPIO
from motor import Car
from music_player import MusicPlayer
from bluedot import BlueDot
from signal import pause


class BluetoothInterface:
    def __init__(self, car, player):
        # interface setups
        self.bluetooth = BlueDot()
        self.bt_interface_code = 0
        self.bt_motor_interface()
        
        # utils
        self.car = car
        self.player = player

        # info for previously pressed button 
        self.music_playing = False
        self.pressed_location = None
        self.pressed_color = None

    def bt_motor_interface(self):
        if self.bt_interface_code == 1:
            # reset modes
            for i in range(self.bluetooth.rows):
                for j in range(self.bluetooth.cols):
                    self.bluetooth[j, i].square = False
                    self.bluetooth[j, i].visible = False
                    self.bluetooth[j, i].when_pressed = None

            # resize
            self.bluetooth.resize(1,1)
            self.bluetooth[0,0].square = False
            self.bluetooth[0,0].visible = True

        self.bluetooth.when_released = self.stop
        self.bluetooth.when_moved = self.slides
        self.bluetooth.when_double_pressed = self.swap_interface
        self.bt_interface_code = 0
        
    def bt_util_interface(self):
        # reset modes
        self.bluetooth.when_released = None
        self.bluetooth.when_moved = None
        self.bluetooth.when_double_pressed = None
        
        # resize
        self.bluetooth.resize(3, 3)

        for i in range(self.bluetooth.rows):
            if i == 0:
                color = (255, 255, 204) # day mode, with brighter music
            elif i == 1:
                color = "blue"
            elif i == 2:
                color = (204, 204, 205) # night mode, with calm music

            for j in range(self.bluetooth.cols):
                self.bluetooth[j, i].color = color


        # row 0: calm musics
        self.bluetooth[0, 0].when_pressed = self.pressed
        self.bluetooth[1, 0].visible = False
        self.bluetooth[2, 0].when_pressed = self.pressed
        
        # row 1: swap interface button
        self.bluetooth[0, 1].visible = False
        self.bluetooth[2, 1].visible = False
        self.bluetooth[1, 1].when_double_pressed = self.swap_interface
        self.bt_interface_code = 1
        
        # row 2: bright musics
        self.bluetooth[0, 2].when_pressed = self.pressed
        self.bluetooth[1, 2].visible = False
        self.bluetooth[2, 2].when_pressed = self.pressed

        # if music is turned on, show in red-color
        if self.music_playing:
            r = self.pressed_location.row
            c = self.pressed_location.col
            self.bluetooth[c, r].color = "red"

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

    def pressed(self, pos):
        # choose song to play
        theme = "calm" if pos.row == 0 else "bright"
        songnum = "1" if pos.col == 0 else "2"
        extension = ".mp3"
        song = theme + songnum + extension
        
        if not self.music_playing:
            # if no music on, turn on the music
            self.player.play(song)
            self.music_playing = True
            self.pressed_location = pos
            self.pressed_color = self.bluetooth[pos.col, pos.row].color
            self.bluetooth[pos.col, pos.row].color = "red"
            print("playing music {}".format(song))

            print(self.pressed_location.col, self.pressed_location.row)
            print(self.pressed_color)

            # check if music has finished
            music_thread = threading.Thread(target = self.checkMusicStatus)
            music_thread.start()
        else:
            # turn off
            if self.pressed_location.row == pos.row and self.pressed_location.col == pos.col:
                self.player.stop()
                self.music_playing = False
                self.bluetooth[pos.col, pos.row].color = self.pressed_color
                print("music {} is turned off.".format(song))


    def checkMusicStatus(self):
        init = True
        while True:
            if self.player.process is not None:
                if self.player.process.poll() == None:
                    if init:
                        print("Music Playing Started")
                        init = False
                    time.sleep(10)
                else:
                    print("Music playing finished")
                    self.music_playing = False
                    self.bluetooth[self.pressed_location.col, self.pressed_location.row].color = self.pressed_color
                    self.player.process = None
                    break
            else:
                break



if __name__ == "__main__":
    car = Car()
    player = MusicPlayer()
    btif = BluetoothInterface(car, player)
    pause()
