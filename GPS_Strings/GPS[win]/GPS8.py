# -*- coding: utf-8 -*-
"""
Created by: 	A.Smith
Date:			2017-08-15
Description:	Python3: USB-Serial comms to uBlox NEO-M8T-Q-10
				Remove all other GPS NMEA string except $GPRMS
				Extract Time/Date/Longitude/Latitude
				
String:
         TIME   V/A   COORD1  N/S  COORD2  E/W        DATE    ERROR
-------------------------------------------------------------------
$GNRMC,130331.00,A,2544.55942,S,02816.91443,E,0.098,,160817,,,A*76
$GNRMC,130332.00,A,2544.55938,S,02816.91442,E,0.098,,160817,,,A*79
-------------------------------------------------------------------
"""
import serial
import sys
from time import sleep

port = "COM11"	# Latte Panda
#port = "COM13"	# Windows PC
baud = 19200

coord = []
Time = []
Lat = []
Lon = []
Date = []
list = ["$PUBX,40,GGA,0,0,0,0*5A\r\n",
		"$PUBX,40,GLL,0,0,0,0*5C\r\n",
		"$PUBX,40,VTG,0,0,0,0*5E\r\n",
		"$PUBX,40,GSV,0,0,0,0*59\r\n",
		"$PUBX,40,GSA,0,0,0,0*4E\r\n",
		"$PUBX,40,ZDA,0,0,0,0*44\r\n"]

def main():
	other = 'string'
	valid = 0									# check if GPRMS string valid
	count = 0									# block of RMS strings
	save  = 0									# save a single RMS string
	ser = serial.Serial(port, baud, timeout=1)	# set up the serial to USB data
	# open the serial port
	if ser.isOpen():
		print(ser.name + ' is open...')			# display com port name
	
	# Eliminate other messages
	for rms in list:
		cmd = rms								# Get command		
		ser.write(cmd.encode('ascii'))	# convert to ASCII [ERROR]
		out = ser.read()						# output to GPS
		sleep(0.005)							# delay 5ms

		#sleep(0.5)
	while True:
		out = ser.read()						# get the unicode byte		
		## python 2.7 ##
		sender = out.decode("utf-8", "ignore")	# 
		#print('{0}'.format(sender)),			# 
		coord.append(sender)					# copy into array
		67890123
		# At each special error check print string
		if sender == '*':
			if save == 1:
				save = 0						# clear flag
				if coord[16] == 'A':			# check for string validation
					print('VALID!!')			# 
					# Extract Data fields
					for i in range (6, 12):
						Time.append(coord[i])	# Time
					for i in range (18, 28):
						Lat.append(coord[i])	# Latitude
					for i in range (31, 42):
						Lon.append(coord[i])	# Longitude
					for i in range (52, 58):
						Date.append(coord[i])	# Date
				
				Times = ''.join(Time)			# 
				print("TIME: {} ".format(Times)),# show single string
				Dates = ''.join(Date)			# 
				print("DATE: {} ".format(Dates)),# show single string
				Lats = ''.join(Lat)				# 
				print("LATITUDE: {} ".format(Lats)),	# show single string
				Lons = ''.join(Lon)				# 
				print("LONGITUDE: {} ".format(Lons)),	# show single string
				
				#clear string after each display
				del Time[:]
				del Times
				del Date[:]
				del Dates
				del Lats
				del Lat[:]
				del Lons
				del Lon[:]
				
				#cmd = raw_input("\nEnter command or 'exit':") 	# python2
				cmd = input("\nEnter command or 'exit':")		# python3
				if cmd == 'q':					# can be 'exit' 
					ser.close()					# close the serial connection
					sys.exit()					# exit()
		# 5 (increase for accuracy) valid RMS string trigger
		elif sender == '$' and save == 0:		# check for valid coordinates
			count = 0							# clear start counter
			valid += 1							# valid counter
			if valid == 5:						# 5 valid coordinates
				valid = 0						# clean counter
				del coord[:]					# clear array & get next line
				save = 1 						# Flag - get next single line $ -> *

if __name__ == '__main__': main()