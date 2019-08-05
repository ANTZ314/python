# -*- coding: utf-8 -*-
"""
Executes a file at file path in default its Application
"""
import subprocess, os, sys

filepath1 = "/home/antz/0Python/files/test.txt"
filepath2 = "/home/antz/Music/00_Downlaods/Horses.mp3"
filepath3 = "/home/antz/0Python/image/File.gif"

def open_file(filename):
	if sys.platform.startswith('linux'):
		subprocess.call(["xdg-open", filename])			# for Linux system
	else:
		os.startfile(filename)							# for Windows
		print("Windows System")

if __name__ == "__main__": open_file(filepath3)
