Halloween "Spooky" Project
=================

The purpose of this project was to improve upon a product that we purchased from BigLots. The product was a very simple speaker with a mat that would play a "spooky" sound anytime somebody stepped on it. The device worked well enough, but the sound (yes only one) was not terriblly spooky, so I decided that it needed to be improved upon.

After setting up the doormat, I decided I wanted to go with a motion sensor to improve the detection. So I have added that to this project since it is basically the same process. There is a lot of reptition in the two code bases, but this is just a quick and dirty implementation so I am not too concerned about code quality.

Hardware Required
-----------------

This system is designed to work with the following hardware:

**halloween-doormat.py**

* [Raspberry Pi](https://www.raspberrypi.org/) (any model with GPIO functionality - which is all of them currently)
* [Pi-Plates DAQCPlate](https://pi-plates.com/) - I used the Pi-Plate because that is what I had on hand already, but any DAC that can interface with the RPi will work. It's up to you to change the code to work with your DAC of choice though.
* A microphone - After some investigation I determined that the "mat" was nothing more than a microphone and that the system just montiored the microphone for voltage changes, and would play the sound when the voltage changed.

**halloween-motion.py**

* [Raspberry Pi](https://www.raspberrypi.org/) (any model with GPIO functionality - which is all of them currently)
* [Adafruit PIR (Motion) Sensor](https://www.adafruit.com/product/189) - You don't have to use this specific one from AdaFruit, but I recommend supporting them since they are pretty awesome (even if not the cheapest around)

Software Required
-----------------

* Python 2.x
* Raspbian (I am running Jessie, but anything else should work too)

See It In Action
----------------

https://youtu.be/sh9OunKbmrY


Batteries Not Included
----------------------

While this code is designed to play a ranom audio file from the current script directory, I didn't include the sounds that I am using. The sounds were created by a friend who is a professional voice over artist, and they aren't mine to give away. Sorry. I am sure you can find your own floating around on the interwebs.

### How it Works

This script is designed to be run from the command line (but I am betting you can set it up to run from rc.local if you wanted to). All it does is attach to the DAC channel and start monitoring the voltages returned from the microphone. When the voltage changes beyond a certain threshold, then we use pygame to play the file.

The system will wait until the audio is done playing before playing another.

Some other minor tweaks: I have made the system monitor which audio files it has most recently played. This is intended to prevent the same random file being played mutliple times in a row.
