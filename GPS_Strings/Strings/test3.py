# -*- coding: utf-8 -*-
"""
Description:
Encode type 'u' to ASCII, then join characters in list and print as string 
"""
import sys
from time import sleep

def run():
	word1 = u'well look at that!'
	word2 = ['w','o','r','d','s',' ','a','n','d',' ','l','i','n','e','s']
	word3 = []
	word4 = 'qwerty,asdf'
	
	#word1.encode('ascii')
	#word1.decode('utf-8')
	type(word1.encode('ascii'))
	print("{}".format(word1))
	
	print("{}".format(word2))
	str1 = ''.join(word2)
	print("{}".format(str(str1)))
	#word3 = word2
	#print("{}".format(word3))
	#del word2
	#print("{}".format(word3))
	#word2 = 'word2'
	#print("{}".format(word2))

	for i in range(1, 5):
		print(word4[i])
	
if __name__ == '__main__': run()