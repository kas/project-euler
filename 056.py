# -*- coding: utf-8 -*-

# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

# realized that using math.pow(a,b) was not letting me get the correct answer, but that a**b was.

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

largest_sum = 0

for a in range(1,100):
	for b in range(1,100):
		current_sum = sum_digits(int(a**b))
		if (current_sum > largest_sum):
			largest_sum = current_sum

print(largest_sum)