# -*- coding: utf-8 -*-
"""
Description: Print the Wikipedia page text referred to in 'search'
			 
Note:		 Language prefix must match the page ("en")
"""
# pip install pattern

from pattern.web import Wikipedia

def main():
	article = Wikipedia(language="en").search('small', throttle=10)
	print article.string

if __name__ == "__main__": main()
