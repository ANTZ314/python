"""
Description:
	Calculates the profit/loss when selling crypto
	Amount put down	[-a, --amount]
	Price bought at [-b, --buy]
	Price sold at 	[-s, --sell]
Usage:
	python cryptoProf2.py -b .0 -s .0 -a .0
	python cryptoProf2.py -b 500.0 -s 650.0 -a 200.0
	python cryptoProf2.py --buy 500.0 --sell 650.0 --amount 200.0
"""
import time 										# 
import sys											# 
import argparse


# Create the parser
my_parser = argparse.ArgumentParser(description='Calculate crypto profit/loss')

# Add the arguments
my_parser.add_argument(	'-b',
						'--buy',
                       	type=float,
                       	help='crypto buy price')

my_parser.add_argument(	'-s',
                       	'--sell',
                       	type=float,
                       	help='crypto sell price')

my_parser.add_argument(	'-a',
                       	'--amount',
                       	type=float,
                       	help='amount spent')

# Execute parse_args()
args = my_parser.parse_args()

def main():
	buy_price	= args.buy							# price per crypto when bought ($)
	sell_price 	= args.sell							# price per crypto when sold ($)
	amount 		= args.amount						# value of purchase ($)
	#buy_price  = 500.00							# price per crypto when bought ($)
	#sell_price = 650.00							# price per crypto when sold ($)
	#amount 	= 200.00							# value of purchase ($)
	inc_dec		= 0.05								# percentage increase/decrease (%)
	diff 		= 0.00								# difference from amount put in
	output		= 0.00								# value of profit/loss

	try:
		print("Amount  ${}".format(amount))
		print("Buy at  ${}".format(buy_price))
		print("Sold at ${}".format(sell_price))

		## If value increased ##
		if sell_price > buy_price:
			inc_dec = sell_price - buy_price
			inc_dec = inc_dec / buy_price
			print("% Gained: {:0.2f}%".format(inc_dec*100))
			diff = (inc_dec * amount)
			print("\nDifference: $ {:0.2f}".format(diff))
			output = amount + diff
			print("${:0.2f} --> ${:0.2f}".format(amount, output))

		## If value decreased ##
		else:
			inc_dec = buy_price - sell_price
			inc_dec = inc_dec / buy_price
			print("Percentage Lost: {:0.2f}%".format(inc_dec*100))
			diff = (inc_dec * amount)
			print("\nDifference: $ {:0.2f}".format(diff))
			output = amount - diff
			print("${:0.2f} --> ${:0.2f}".format(amount, output))

		## End the run
		sys.exit(0)


	# Ctrl+C will exit the program correctly
	except KeyboardInterrupt:
		print("\r\nEXIT PROGRAM!!")					# Pistol whip Thomas Wayne
		sys.exit(0)									# Take Martha's pearls

if __name__ == "__main__":	main()