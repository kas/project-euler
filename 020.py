# -*- coding: utf-8 -*-

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# found out how to have utf-8 character encoding in python file

num = 100	# number we want to find the sum of the digits of
factorial = 1	# starting number the we multiply on to find the factorial
sum = 0	# starting number that we add to to find the sum

for x in range(num, 0, -1):	# x goes from 100 to 0
	factorial*=x	# multiply factorial by x each iteration

for x in range(0,len(str(factorial))):	# x goes from first digit to last digit in factorial
	sum+=int(str(factorial)[x]) # add each digit to sum

print sum