"""
CRYPTO CSV PRE-PROCESSING:
	-> READ DATA TO ARRAYS (30 points)	| .
	-> CHECK DATA TYPES					| x
	-> SET TO 2 DECIMAL PLACES			| x
	-> PLOT SINGLE CHART				| x
	-> PLOTTING VALUES					| x
	-> WRITE LISTS BACK INTO CSV 		| .

Insert Latest Data:
	-> Download latest ETH & BTC
	-> Copy from last date to current date
	-> Ctr + Shift + V
	-> Click "shift down"
	-> Delete extra cell 

NOTE:
	-> Using file "BTC_ETH1.csv"
	-> Remove numbered column
	-> Add headings: DATE | BTC_OPEN | ETH_OPEN

Use:
	-> python plot4.py
"""

import csv, time, sys
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


file1 = "crypto/BTC_ETH3.csv"

DATE2 = []


#########################
## READ DATA TO ARRAYS ##
#########################
#column_names = ["DATE", "BTC_OPEN", "ETH_OPEN"]
df = pd.read_csv(file1)#, names=column_names)
#print(df)

DATE = df.DATE.to_list()
BTC_OPEN = df.BTC_OPEN.to_list()
ETH_OPEN = df.ETH_OPEN.to_list()

## Remove time from String ##
for i in DATE:
	DATE2.append(i.split(' ')[0])
DATE = DATE2


#############################
## SET TO 2 DECIMAL PLACES ##
#############################
BTC_OPEN = list(np.around(np.array(BTC_OPEN),2))
ETH_OPEN = list(np.around(np.array(ETH_OPEN),2))


#####################
## PLOTTING VALUES ##
#####################

#t = np.arange(0.01, 48.0, 0.01) 		# Set the range to number of rows?
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in DATE]	# X-Axis
#data1 = BTC_OPEN												# 1st Y-Axis 
#data2 = ETH_OPEN												# 2nd Y-Axis 


## GET TOP 30 DATA ELEMENTS ##
date  = DATE[:30]
data1 = BTC_OPEN[:30]
data2 = ETH_OPEN[:30]


## FLIP THE DATA ##
date  = date[::-1]
data1 = data1[::-1]
data2 = data2[::-1]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.tick_params(axis='x', rotation=90)
ax1.set_ylabel('BTC_OPEN', color=color)
ax1.plot(date, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('ETH_OPEN', color=color)
ax2.plot(date, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 		# otherwise the right y-label is slightly clipped

print("Show Plot")
plt.show()


print("Executed Successfully...")
sys.exit(0)	