# -*- coding: utf-8 -*-
"""
Trying to save each input character into string or list
"""
import sys
from time import sleep

list = ['qwerty',
		'asdfgh',
		'zxcvbn']

def main():
	a = 0x10
	b = 0x10

	words = "ANTZ"
	print("Original: " + words)

	## Python2 - convert to hex
	words = words.encode("hex")
	print("Hex:" + words)

	## Python2 - convert back to string
	words = words.decode("hex")
	print("Decoded: " + words)

	## Little Endian ASCII string:
	words = ''.join(reversed(words))
	print("Inverted: " + words)

	## Python2 - convert to hex
	words = words.encode("hex")
	print("Hex:" + words)

	## Little Endian Hex string:
	#words = ''.join(reversed(words))
	#print("Inverted: " + words)

	## Concatenate all values to one large Hex value:
	words = hex( (a<<8) | b )
	print("Single Hex: " + words)

	## Convert to Integer:

	print("Integer: ")

	## Python2 - convert back to string
	#words = words.decode("hex")
	#print("Decoded: " + words)

	print("Exit!")
	sys.exit(0)

if __name__ == '__main__': main()
