"""
Description:
	Hnaldes multiple types of ERRORS
"""
import sys						# system things


###################
## MAIN FUNCTION ##
###################
def main():
	
	try:
		###########################
		## INSERT MAIN CODE HERE ##
		###########################
			
		
	## System Error: ##
	except OSError as err:
		print ("\r\nOS ERROR {}".format(err))
		sys.exit()
	## Value Error ##
	except ValueError:
		print("\r\nError with variable...")
		sys.exit()
	## Keyboard Exit ##
	except KeyboardInterrupt:
		print("\r\nEscape (MAIN) - Device Closed...")
		sys.exit(0)	
	## NameError - Suggested ##
	except NameError:
		print("\r\nNameError:")
		sys.exit(0)	
	## Unknown Error ##
	except:
		print("\r\nUnexpected Error:", sys.exc_info()[0])
		sys.exit() 
	
	## Exit Properly when finished ##
	finally:
		print("Closed Device - Final!!")
		sys.exit(0)	

if __name__ == "__main__":	main()
