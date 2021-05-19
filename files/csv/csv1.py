"""
Description:
* Open CSV file, print contents, close file
* commented - write to file
"""

import csv, time, sys


file1 = "crypto/BTC.csv"


file = open(file1, 'r') 
print (file.read())
file.close()
	
			
print("WAIT...")
time.sleep(2)
			
			
#with open("file2.csv", "+a") as f:
#			w = csv.writer(f)
#			w.writerow(sensorData.values())

print("Exit")
sys.exit(0)	
