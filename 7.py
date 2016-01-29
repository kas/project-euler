# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def findPrimeNumbers(number): # find the 10,001st prime number
	array=[2,3,5,7,11,13] # contains first 6 prime numbers
	y=15
	while len(array)<10001:
		print len(array)
		for x in reversed(range(1, y, 2)):
			if(y%x==0 and x!=1): # y is not a prime number
				break
			elif(x==1): # y is a prime number
				array.append(y)
		y+=2 # go to next odd number
	print array[-1]
		
findPrimeNumbers(10001)