#!/usr/bin/python3
#
# Name: onehundred.py
# Auth: Frank Cass
# Date: 20170430
# Desc: Count from 1 to 100 while outputting at the quarter, halfway and three quarter mark.
#
###

import time

n = 1

def count(n):
	if  n >= 100:
		print ("We've reached the limit!")
	elif n < 100:
		if n == 25:
			print ("We're a quarter of the way there!")
		elif n == 50:
			print ("We're half way there!")
		elif n == 75:
			print ("We're three quarters of the way there!")
		else:
			print ("Here's where we're at",n)

while n <= 100:
	count(n)
	n = n + 1
	time.sleep (0.1)
