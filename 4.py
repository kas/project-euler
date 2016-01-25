def palindrone(product):
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

array = []

for x in range(100,999):
 	for y in range(100,999):
 		if (palindrone(x*y)):
 			array.append(x*y)

print sorted(array)[-1]