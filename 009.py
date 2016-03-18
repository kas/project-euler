# -*- coding: utf-8 -*-

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1,1001):
	for b in range(1,1001):
		for c in range(1,1001):
			if ((pow(a,2)+pow(b,2))==pow(c,2) and (a<b) and (b<c)):
				if ((a+b+c)==1000):
					print(a*b*c)