# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:33:49 2017
@author: antz
"""
import random
import urllib.request

def download_web_image(url):
	name = random.randrange(1, 1000)
	full_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url, full_name)
	
download_web_image("http://stories-and-trends.gettyimages.netdna-cdn.com/wp-content/uploads/2015/09/GettyImages-516422197.jpg")
