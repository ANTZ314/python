"""
Description:
Standard Bank Tax Free Call Account = 3.5%(+) interest rate
Calculates wealth accrued by depositing the maximum amount of R30 000 annually for 'x' years
"""
import time 					## Import 'time' library. Allows us to use 'sleep'
import sys

def main():
	years = 0 						# number of years
	annual_inv = 30000				# R30k max per year
	interest = 0					# interest added
	total = 0 						# total wealth accrued
	n = 1							# no. times per period
	t = 1							# no. times period elapsed
	r = 0.035						# 3.5% interest rate

	try:
		while years < 20:
			## maximum investment each year
			total = total + annual_inv

			## Annual compound interest 5%
			#total = total*(1+(r/n)**(n*t))
			interest = total*(((1+r)**n)-1)
			total = total + interest

			print("Year: {} Total: {}".format(str(years+1), str(total)))
			time.sleep(1)			## Wait
			years += 1				# decrement

		## End the run
		sys.exit(0)


	# Ctrl+C will exit the program correctly
	except KeyboardInterrupt:
		print("\r\nEXIT PROGRAM!!")					# Pistol whip Thomas Wayne
		sys.exit(0)									# Take Martha's pearls

if __name__ == "__main__":	main()