# -*- coding: utf-8 -*-

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

# realized that my palindrone and palindroneString methods (from problem 004) won't work in Python 3

# from problem 004
def palindrone(product): # returns whether passed product is palindrone or not
	numOfDigits = len(str(product))
	isPalindrone=False

	if numOfDigits%2==0: # if even number of digits
		half=numOfDigits/2
		if str(product)[:half][::-1]==str(product)[half:]:
			isPalindrone=True

	else: # if odd number of digits
		half=numOfDigits/2 # if 5 digits, is equal to 2
		if str(product)[:half][::-1]==str(product)[half+1:]:
			isPalindrone=True

	return isPalindrone

# from problem 004, modified to accept strings
def palindroneString(product): # returns whether passed product is palindrone or not
	numOfDigits = len(product)
	isPalindrone=False

	if numOfDigits%2==0: # if even number of digits
		half=numOfDigits/2
		if product[:half][::-1]==product[half:]:
			isPalindrone=True

	else: # if odd number of digits
		half=numOfDigits/2 # if 5 digits, is equal to 2
		if product[:half][::-1]==product[half+1:]:
			isPalindrone=True

	return isPalindrone

numbers = []

for x in range(0,1000000):
	if palindrone(x):
		binary = "{0:b}".format(x)
		if palindroneString(binary):
			numbers.append(x)

print("sum: ",sum(numbers))