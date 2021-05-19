# -*- coding: utf-8 -*-
"""
Description:
Basic framework for "main.py" file calling and instantiating 2 separate classes
Printing something from each one, with start print also
"""
import sys
import ClassTest1 as class1

def main():
	classi = class1.ClassTest1() 

	classi.message1("hey")

if __name__ == "__main__": main()

