"""
Description:
	- Calculates total investment + interest accrued for each year
	- Continuous monthly installments = annual amount
	- Calculates Total + annual compound interest

Note:
	- Set values in code

Use:
	- python interest1.py
"""
import time 										# 
import sys											# 


def main():
	withdraw = 5									# return period for withdrawel
	inv_amount = 1000								# R12k per year (R1000 per month)
	years = 0 										# number of years
	months = 12										# number of months in a year
	interest = 0									# interest added
	total = 0 										# total wealth accrued
	n = 1											# no. times per period
	t = 1											# no. times period elapsed
	r = 0.041										# 3% interest rate (above inflation)

	try:
		print("R{} per month @ {:0.2f}% interest".format(inv_amount, (r*100)))
		
		## maximum investment each year
		inv_amount = inv_amount * months			# get annual amount

		while years < withdraw:
			## maximum investment each year
			total = total + inv_amount

			## Annual compound interest ##
			#total = total*(1+(r/n)**(n*t))
			interest = total*(((1+r)**n)-1)
			total = total + interest

			print("Year: {} Total: {:0.2f}".format(str(years+1), total))
			time.sleep(1)							## Wait
			years += 1								# decrement
		
		## End the run
		sys.exit(0)


	# Ctrl+C will exit the program correctly
	except KeyboardInterrupt:
		print("\r\nEXIT PROGRAM!!")					# Pistol whip Thomas Wayne
		sys.exit(0)									# Take Martha's pearls

if __name__ == "__main__":	main()