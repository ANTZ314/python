# -*- coding: utf-8 -*-
"""
Description:
Get time and date seperately

Usage:
python dateTime.py
"""
from datetime import datetime

""" MAIN FUNCTION """
def main():
	now = datetime.now()							# Get 'nows' date & time
	current_date = now.strftime("%Y-%m-%d")			# Extract date
	current_time = now.strftime("%H:%M:%S")			# Extract time

	print(now)
	print("Date: {}".format(current_date))
	print("Time: {}".format(current_time))
	

		
if __name__ == "__main__": main()