import subprocess
import signal
import threading
import time, os

class MusicPlayer:
    def __init__(self):
        subprocess.call('pwd', shell=True)
        subprocess.call('ls ./assets', shell=True)
        self.process = None

    def play(self, song):
        if self.process is not None:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
        song_loc = "./assets/" + song

        self.process = subprocess.Popen(
                args = ["omxplayer", song_loc], 
                preexec_fn = os.setsid,
                )
       
    def stop(self):
        print("killing proc {} pid {} os {}".format(self.process, self.process.pid, os.getpgid(self.process.pid)))
        os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
        self.process = None

if __name__ == "__main__":
    player = MusicPlayer()
    player.play("calm1.mp3")
    time.sleep(5)
    player.stop()
