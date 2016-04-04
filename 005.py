# -*- coding: utf-8 -*-

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def findNumber():
	found=False
	x=2520 # multiples of this number are already divisible by 1-10

	while found==False:
		for y in range(11,21): # try dividing x by 11-20 without remainer
			if (x%y==0):
				if (y==20):
					found=True
					return x
			else:
				break
		x+=2520

print("FINAL",findNumber())