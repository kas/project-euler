# coding: utf-8

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

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

array = [] # blank array to store all palindrones in range

for x in range(100,1000):
 	for y in range(100,1000):
 		if (palindrone(x*y)):
 			array.append(x*y) # add each palindrone to array

print sorted(array)[-1] # sort array and print last (largest) palindrone