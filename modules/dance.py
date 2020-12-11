from motor import Car
from music_player import MusicPlayer
import sys, getopt, time
import threading


def dance_to_bright1(car, music_player):
	music_player.play("bright1.mp3")
	time.sleep(12)

	for i in range(79):
		car.clockwise(t = 0.25, duty_cycle = 80)
		time.sleep(0.25)
		car.counterClockwise(t = 0.25, duty_cycle = 80)
		time.sleep(0.25)

def dance_to_bright2(car, music_player):
	music_player.play("bright2.mp3")
	time.sleep(12)

	for i in range(23):
		car.forward(t = 1, duty_cycle = 50)
		time.sleep(1)
		car.backward(t = 1, duty_cycle = 50)
		time.sleep(1)



def main(argv):

	# 1. get input file argument
	MUSICFILE = ""

	try:
		opts, args = getopt.getopt(argv,"m:",["music_file="])
	except getopt.GetoptError:
		print ('dance.py -m <filename>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-m':
			MUSICFILE = arg

	print("FILENAME: {}".format(MUSICFILE))
	if MUSICFILE == "":
		print("error in argument passing")
		return 1

	# 2. play
	if MUSICFILE != "bright1.mp3" and MUSICFILE != "bright2.mp3":
		print("MUSIC '{}' is not supported, or file does not exist".format(MUSICFILE))
	else:
		car, music_player = Car(), MusicPlayer()
		if MUSICFILE == "bright1.mp3":
			dance_to_bright1(car, music_player)
		if MUSICFILE == "bright2.mp3":
			dance_to_bright2(car, music_player)

	return 0

if __name__ == "__main__":
	main(sys.argv[1:])
