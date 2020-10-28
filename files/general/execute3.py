# -*- coding: utf-8 -*-
"""
Description:
Calling another file from this file
"""
==================================================
One way:
==================================================
import os
import fileB

def main():	
	fileB.subroutine()

if __name__ == '__main__':
    main()

 ==================================================
Another way:
 ==================================================
 import os

def main():	
	os.system('python fileD.py')

if __name__ == '__main__':
    main()