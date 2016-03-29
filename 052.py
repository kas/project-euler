# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

for x in range(1,1000001):
	original = sorted(list(int(digit) for digit in str(x)))
	for y in range(2,7):
		multiple = x*y
		permutedMultiple = sorted(list(int(digit) for digit in str(multiple)))
		if (original != permutedMultiple):
			break
		elif ((original == permutedMultiple) and (y == 6)):
			print(x)