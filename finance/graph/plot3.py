"""
CRYPTO CSV PRE-PROCESSING:
	-> READ DATA TO ARRAYS (ALL)		| x
	-> CHECK DATA TYPES					| x
	-> SET TO 2 DECIMAL PLACES			| x
	-> PLOT SINGLE CHART				| x
	-> PLOTTING VALUES					| x
	-> WRITE LISTS BACK INTO CSV 		| .

Insert Latest Data:
	-> Download latest ETH & BTC
	-> Copy from last date to current date
	-> left click -> special paste -> "shift down"
	-> Delete extra cell
Note:
	-> Remove numbered column
	-> Add headings: DATE | BTC_OPEN | ETH_OPEN
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


"""
######################
## CHECK DATA TYPES ##
######################
print(type(DATE[12]))					# check random value type
print(type(BTC_OPEN[12]))				# check type is now float (2 decimal)
print(type(ETH_OPEN[12]))				# check type is now float (2 decimal)

## CONVERT ARRAY TO FLOAT - UNECESSARY ##
#list(np.float_(BTC_OPEN))
#list(np.float_(ETH_OPEN))
"""

#############################
## SET TO 2 DECIMAL PLACES ##
#############################
BTC_OPEN = list(np.around(np.array(BTC_OPEN),2))
ETH_OPEN = list(np.around(np.array(ETH_OPEN),2))


"""
#######################
## PLOT SINGLE CHART ##
#######################
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in DATE]
y = range(len(x))
y = BTC_OPEN

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()
"""

#"""
#####################
## PLOTTING VALUES ##
#####################
#t = np.arange(0.01, 48.0, 0.01) 		# Set the range to number of rows?
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in DATE]	# X-Axis
data1 = BTC_OPEN												# 1st Y-Axis 
data2 = ETH_OPEN												# 2nd Y-Axis 


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.set_ylabel('BTC_OPEN', color=color)
ax1.plot(x, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('ETH_OPEN', color=color)
ax2.plot(x, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout() 		# otherwise the right y-label is slightly clipped

print("Show Plot")
plt.show()
#"""

###############################
## WRITE LISTS BACK INTO CSV ##
###############################
df = pd.read_csv(file1)  ## 1.csv is the csv file I want to import. 

#a = [0.001, 5, 38, 70, 101, 140, 190]
#b = [35, 65,  100, 160, 170, 200]

df['DATE'] 		= DATE
df['BTC_OPEN'] 	= BTC_OPEN
df['ETH_OPEN'] 	= ETH_OPEN

df.to_csv(file1)


print("Executed Successfully...")
sys.exit(0)	