-------------------------------------------
Working folder for TimeLapse Project final:
-------------------------------------------

Path to saved folder:
/home/antz/Documents/00_PERSONAL/RasPi/00_PiCam/timelapse/TL1

------------
Description:
------------
tl_main.py		- Main file

LED.py			- Multiple LED blink functions [7x modes]

usb.py			- Checks for USB device, if found,
			- Moves the specified file (if exists) to the USB path

convert.py		- Converts the folder of .jpg to mp4 file
			- auto-remove USB safely

quit.py			- Empty timelapse pictures folder
			- Close necessary running processes
			- shutdown properly (bash file)


============
STILL TO DO:
============

On startup:
	- Check pictures folder contents
		-> if files, clear folder (premature power-off)
	- Set switch as Standbye Mode regardless of status

Future use classes:
	- usb check and copy to class
	- convert folder of jpg into mp4 file
	- Auto-remove usb safely
	- close all running processes & shutdown
		-> Empty pictures folder
	- Diff LED blink colours [x7]


	
