# -*- coding: utf-8 -*-
"""
Trying to save each input character into string or list
"""
import sys
from time import sleep

words = "qwerty-asdfgh"

list = ['qwerty',
		'asdfgh',
		'zxcvbn']

def main():
	## Python2
	print(hex(ord("c")))
	print(format(ord("c"), "x"))
	print("c".encode("hex"))
	## Python3
	#print(codecs.encode(b"c", "hex"))

if __name__ == '__main__': main()
