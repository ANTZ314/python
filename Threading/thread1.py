# -*- coding: utf-8 -*-
"""
author: 
Antony Smith

description: 
Threading Tutorial - Run to functions concurrently 
-> different to Multiprocessing

Run:
python3 thread1.py
"""
import threading 
import time
#import ClassName as Class

# For timing the code being run
start = time.perf_counter()			

def do_somthing():
	print("sleeping 1 second...")
	time.sleep(1)
	print("Done...")

def main():
	print("Start...")

	# create thread objects
	t1 = threading.Thread(target=do_somthing)
	t2 = threading.Thread(target=do_somthing)

	# Run the individual threads:
	t1.start()
	t2.start()

	# This method will make sure the Threads are completed,
	# before finishing the rest of the code:
	t1.join()
	t2.join()

	finish = time.perf_counter()
	print("Finished in {} second(s)".format(round(finish-start, 2)))
    
if __name__ == "__main__": main()