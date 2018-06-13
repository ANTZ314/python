# -*- coding: utf-8 -*-
"""
From received/extracted ASCII string:
	-> Convert to little Endian
	-> Convert to single Hex value
	-> Convert to Integer value
"""
import sys
import binascii

def main():
	#new = []
	temp = "qwerty"
	words = "ANTS"
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

	## Conert string to single hex value:
	words = binascii.hexlify(bytearray(words))
	print("Hex String: " + words)

	## Create Array of each character:
	#new = list(words)
	#for x in range(len(new)):
	#	print("Split: " + new[x])

	## Python2 - convert each char to hex
	#for x in range(len(new)):
	#	new[x] = new[x].encode("hex")
	#	print("Hex:" + new[x])

	## Convert to Integer:
	i = int(words, 16)
	print("Integer: " + str(i))

	temp = "0D1116FA"
	i = int(temp, 16)
	print("Integer: " + str(i))

	print("Exit!")
	sys.exit(0)

if __name__ == '__main__': main()
