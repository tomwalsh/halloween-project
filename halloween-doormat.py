#!/usr/bin/python
import signal
import sys
import pygame
import piplates.DAQCplate as DAQC
import time
from os import listdir
from random import choice

audiotypes = { "wav" }
DACport = 0

lastfiles = []

def main():
	signal.signal(signal.SIGINT, signal_handler)
	while True:
		value = round(DAQC.getADC(0, DACport), 2)
		print value
		if (value < 3.20) or (value > 3.39) :
			print "Value " + str(value) + ", Activated!"
			DAQC.setDOUTbit(0,0)
			playAudio()
			DAQC.clrDOUTbit(0,0)
		else:
			print "Value " + str(value) + ", Waiting..."
		time.sleep(0.1)
	GPIO.cleanup()

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
	DAQC.clrDOUTbit(0,0)
	sys.exit(0)

if __name__=="__main__":
	main()
