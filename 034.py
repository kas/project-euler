# -*- coding: utf-8 -*-

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

numbers = []

for x in range(3,1000000):
	print(x)
	currentSum = 0
	for digit in str(x):
		currentSum+=math.factorial(int(digit))
	if (currentSum==x):
		numbers.append(x)

print("sum: ",sum(numbers))