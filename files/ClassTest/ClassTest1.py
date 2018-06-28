# -*- coding: utf-8 -*-
"""
Description:

"""
import ClassTest2 as class2

class ClassTest1: 
	def __init__(self, **kwargs):
		print("Class1 init!!")

	def message1(self, string):
		print("Message: " + str(string))
		
		classii = class2.ClassTest2()
		classii.message2("NOW")

