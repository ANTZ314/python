# -*- coding: utf-8 -*-
"""
Description:

Usage:
python rename.py /home/antz/0_samples/scrapy pic.jpg
"""
import os
import sys

# checking whether path and filename are given.
if len(sys.argv) != 3:
    print "Usage : python rename.py <path> <new_name.extension>"
    sys.exit()

# splitting name and extension.
name = sys.argv[2].split('.')
if len(name) < 2:
    name.append('')
else:
    name[1] = ".%s" %name[1]

""" MAIN FUNCTION """
def main():
	# to name starting from 1 to number_of_files.
	count = 1

	# creating a new folder in which the renamed files will be stored - NO NEED OVER-WRITE!
	#s = "%s/new_name" % sys.argv[1]
	#print "creating folder" + s
	#try:
	#    os.mkdir(s)
	#except OSError:
	    # if pic_folder is already present, use it.
	#   pass

	try:
	    for x in os.walk(sys.argv[1]):
	    	
	        for y in x[2]:
	            # creating the rename pattern
	            s = "%s/%s%s%s" %(x[0], name[0], count, name[1])
	            
	            # getting the original path of the file to be renamed
	            z = os.path.join(x[0],y)
	            #print "file path: " + z
	            #print "new file: " + s
	            
	            # RENAMING
	            os.rename(z, s)
	            # incrementing the count
	            count = count + 1
	    print"DONE!"
	except OSError:
	    pass
	

		
if __name__ == "__main__": main()