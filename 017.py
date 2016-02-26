# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ones=["","one","two","three","four","five","six","seven","eight","nine"]

tens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

ty=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

big=["","","","hundred","thousand"]

string="" # blank string, will append to it later

def thousand(num):
	one(num[0])
	global string
	string+=' '
	string+=big[len(num)]
	if (int(num[1:])>=1):
			string+=" and "

	hundred(num[1:])

def hundred(num):
	if (int(num[0])>=1):
		one(num[0])
		global string
		string+=' '
		string+=big[len(num)]
		if (int(num[1:])>=1):
			string+=" and "

	ten(num[1:])

def ten(num):
	global string
	if (int(num[0])==1):
		string+=tens[int(num[1])]
	else:
		if (int(num[0])>1):
			string+=ty[int(num[0])]
			if (int(num[1])>=1):
				string+='-'
		one(num[1:])

def one(num):
	global string
	string+=ones[int(num[0])]

for x in range(1,1001):
	if (len(str(x))<=1): # 1-9 method
		# do ones[x]

		one(str(x))

	elif (len(str(x))<=2): # 10-99 method
		# if first number is <= 1
			# do tens[x]
		# elif first number > 1
			# do ty[x]
			# add '-'
		# remove leading character and pass the rest to 1-9 method

		ten(str(x))

	elif (len(str(x))<=3): # 100-999 method
		# do ones array
		# do big[x]
		# add "and"
		# remove leading character and pass the rest to 10-99 method

		hundred(str(x))

	elif (len(str(x))<=4): # 1000-1001 method
		# do ones array
		# do big[x]
		# add "and"
		# remove leading character and pass the rest to 100-999 method

		thousand(str(x))

	# string+='\n'

# print string

count = 0 # counter variable, counts how many characters are in string

for x in range(0,len(string)): # iterates from string[0] to the end of the string
	if (string[x]!=' ' and string[x]!='-'): # do not count space and dash characters
		count+=1

print count