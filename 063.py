# -*- coding: utf-8 -*-

# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

numbers = []

for x in range(1,101):
	for y in range(1,101):
		if (len(str(x**y))==y):
			numbers.append(x**y)

print("length: ",len(numbers))