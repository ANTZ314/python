# -*- coding: utf-8 -*-
import serial
from time import sleep
import sys

port = "COM11"
baud = 19200

list = ["$PUBX,40,GGA,0,0,0,0*5A\r\n",
		"$PUBX,40,GLL,0,0,0,0*5C\r\n",
		"$PUBX,40,VTG,0,0,0,0*5E\r\n",
		"$PUBX,40,GSV,0,0,0,0*59\r\n",
		"$PUBX,40,GSA,0,0,0,0*4E\r\n",
		"$PUBX,40,ZDA,0,0,0,0*44\r\n"]

def run():
	count = 0
	ser = serial.Serial(port, baud, timeout=1)
	# open the serial port
	if ser.isOpen():
		print(ser.name + ' is open...')
	
	# Eliminate other messages
	for rms in list:
		cmd = rms								# Get command 
		ser.write(cmd.encode('ascii'))	# convert to ASCII
		out = ser.read()						# output to GPS
		sleep(0.005)							# delay 5ms
	
	while True:
		out = ser.read()
		print(out, end="")						# python3
		#print(out),							# python2
	
	print('exit!!')
	sys.exit(0)
		
if __name__ == '__main__': run()
