"""
Description:
	Based on price bought & sold
	Calculates the profit/loss when selling crypto

Usage:
	python cryptoProfit.py
"""
import time 										# 
import sys											# 


def main():
	buy_price  	= 500.00								# price per crypto when bought ($)
	sell_price 	= 650.00								# price per crypto when sold ($)
	amount 		= 200.00								# value of purchase ($)
	inc_dec		= 0.05									# percentage increase/decrease (%)
	output		= 0.00									# value of profit/loss

	try:
		print("Bought at ${}".format(buy_price))
		print("Sold at   ${}".format(sell_price))

		## If value increased ##
		if sell_price > buy_price:
			inc_dec = sell_price - buy_price
			inc_dec = inc_dec / buy_price
			#inc_dec = 150.00 / 500.00
			print("% Gained: {:0.2f}".format(inc_dec))
		## If value decreased ##
		else:
			inc_dec = buy_price - sell_price
			print("Percentage Lost: {:0.2f}".format(inc_dec))


		output = (inc_dec * amount) + amount
		print("\n${} -> ${}".format(amount, output))

		## End the run
		sys.exit(0)


	# Ctrl+C will exit the program correctly
	except KeyboardInterrupt:
		print("\r\nEXIT PROGRAM!!")					# Pistol whip Thomas Wayne
		sys.exit(0)									# Take Martha's pearls

if __name__ == "__main__":	main()