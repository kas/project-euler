# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

num = 600851475143 # number we are finding largest prime factor of

x = 2 # iterator variable
while x * x < num: # only use products less than the number
	while num % x == 0: # only use values of x that divide the number evenly
		num = num / x # make number smaller
	x = x + 1 # iterate x
print num