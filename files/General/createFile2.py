# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:44:39 2017
@author: antz
https://www.youtube.com/watch?v=YV6qm6erphk&index=23&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&spfreload=10
"""
fw = open('sample.txt', 'w') # creat the file and write
fw.write('write some text to the sample file\n')
fw.write('more sample text to the file\n')
fw.close()  # close the file and free the memory