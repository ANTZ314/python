# -*- coding: utf-8 -*-
"""
Description:
Append, and print of lists, strings
"""
import sys
from time import sleep

word = 'fuck you'
words = ['w','o','r','d','s',' ','a','n','d',' ','l','i','n','e','s']
word2 = []

def run():
	for i in words:
		word2.append(i)	#words[i]
		
	print("{}".format(word2))
	
	for j in range(0,len(words)):
		print(word2[j]),

	choice = input("Exit\r\n")
	if choice == 'q':
		print('\r\nexit!!')
		sys.exit(0)
	
if __name__ == '__main__': run()