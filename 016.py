# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

power=1000

num=2
sum=0

for x in range(2,power+1): # start at 2^2
	num*=2

# num is now 2^1000

for x in range(0,len(str(num))): # get each digit in num
	sum+=int(str(num)[x]) # add each digit of num to sum

print sum