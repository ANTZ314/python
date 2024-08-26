# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:59:42 2017

@author: antz
"""
import matplotlib.pyplot as plt
#from PIL import Image
import PIL

## WORKS ##
image = PIL.Image.open('/home/antz/0_samples/colour/games.png')
image.show()


## Works but does not display (command window?) ##
img = PIL.Image.open('/home/antz/0_samples/colour/tacks.jpg')
plt.imshow(img)

print("complete")