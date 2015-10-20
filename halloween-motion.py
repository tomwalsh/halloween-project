#!/usr/bin/python
import signal
import sys
import pygame
import time
from os import listdir
from random import choice
import RPi.GPIO as io

audiotypes = { "wav" }
lastfiles = []
pir_pin = 23

io.setmode(io.BCM)

def main():
	io.setup(pir_pin, io.IN)
	signal.signal(signal.SIGINT, signal_handler)
	while True:
		if io.input(pir_pin):
			print "Activated!"
			playAudio()
		else:
			print "Waiting..."
		time.sleep(0.1)
	io.cleanup()

def playAudio():
	global lastfiles
	myfile = randomFile("./")
	if( len(lastfiles) > 2):
		lastfiles = lastfiles[1:len(lastfiles)]
	lastfiles.append(myfile)
	print "Playing file " + myfile
	pygame.mixer.init()
	pygame.mixer.music.load(myfile)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

def isValidAudio(filename):
	global lastfiles
	filename = filename.lower()
	if filename in lastfiles:
		return False
	return filename[filename.rfind(".")+1:] in audiotypes

def randomFile(dir):
	audiofiles = [f for f in listdir(dir) if isValidAudio(f)]
	return choice(audiofiles)

def signal_handler( signal, frame ):
	pygame.mixer.stop()
	sys.exit(0)

if __name__=="__main__":
	main()
