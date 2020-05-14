# -*- coding: utf-8 -*-
"""
author: Antony Smith

description: 

Path: cd /home/antz/GIT314/python/threading

Run: python3 timethread1.py
"""
import threading
import time
t = None

def sayHello():
	while True:
		print "Hello!",
		time.sleep(1)

def main():
	global t

	print "start!"
	t = threading.Timer(5, sayHello)
	t.start()
	print "stop!"
    
if __name__ == "__main__": main()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Note!! - Gets stuck in this with no exit.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~