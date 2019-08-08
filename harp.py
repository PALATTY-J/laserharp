# LASER harp
# Author :Rituparna Matkar
# Edited By: Palatty Jesvin Joseph 
# for Arduino UNO
# This script reads the inputs from the serial port and play notes accordingly
import pygame, serial, time

numpins = 5
previnputs = [False for a in range(0, numpins)]

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except:
    ser= serial.Serial('/dev/ttyACM1', 9600)

pygame.mixer.pre_init(channels=6, buffer=1024)
pygame.mixer.init()

guit_let = ["c1", "d", "e", "f", "g", "a"]
guitar_notes = [pygame.mixer.Sound("samples/"+letter+".wav") for letter in guit_let]


def guitar(i):
	guitar_notes[i].play()
	print guit_let[i]
count = 0

while True:
    
    line = ""
    if True:
        line = ser.readline()
    else:
        line = raw_input()
    line = line.strip('\n')
    line += ser.readline() 
    for i in range(0, numpins):
        curr = line[i] != '0'
        prev = previnputs[i]
        if curr and not prev:
            guitar(i)
        previnputs[i] = curr
