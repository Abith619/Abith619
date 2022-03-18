"""While the popularity of cheques as a payment method has diminished in recent years, some companies 
still issue them to pay employees or vendors. The amount being paid normally appears on a cheque 
twice, with one occurrence written using digits, and the other occurrence written using English 
words. Repeating the amount in two different forms makes it much more difficult for an unscrupulous 
employee or vendor to modify the amount on the cheque before depositing it. In this exercise, your 
task is to create a function that takes an integer between 0 and 999 as its only parameter, and 
returns a string containing the English words for that number. For example, if the parameter to 
the function is 142 then your function should return “one hundred forty two”. Use one or more 
dictionaries to implement your solution rather than large if/elif/else constructs. Include a 
main program that reads an integer from the user and displays its value in English words"""

def convert_to_words(num):
	l = len(num)
	if (l == 0):
		print("empty string")
		return
	if (l > 4):
		print("Length more than 4 is not supported")
		return
	single_digits = ["zero", "one", "two", "three",
					"four", "five", "six", "seven",
					"eight", "nine"]
	two_digits = ["", "ten", "eleven", "twelve",
				"thirteen", "fourteen", "fifteen",
				"sixteen", "seventeen", "eighteen",
				"nineteen"]
	tens_multiple = ["", "", "twenty", "thirty", "forty",
					"fifty", "sixty", "seventy", "eighty",
					"ninety"]
	tens_power = ["hundred", "thousand"]
	print(num, ":", end=" ")
	if (l == 1):
		print(single_digits[ord(num[0]) - 48])
		return
	x = 0
	while (x < len(num)):
		if (l >= 3):
			if (ord(num[x]) - 48 != 0):
				print(single_digits[ord(num[x]) - 48],
					end=" ")
				print(tens_power[l - 3], end=" ")
			l -= 1
		else:
			if (ord(num[x]) - 48 == 1):
				sum = (ord(num[x]) - 48 +
					ord(num[x+1]) - 48)
				print(two_digits[sum])
				return
			elif (ord(num[x]) - 48 == 2 and
				ord(num[x + 1]) - 48 == 0):
				print("twenty")
				return
			else:
				i = ord(num[x]) - 48
				if(i > 0):
					print(tens_multiple[i], end=" ")
				else:
					print("", end="")
				x += 1
				if(ord(num[x]) - 48 != 0):
					print(single_digits[ord(num[x]) - 48])
		x += 1
a=convert_to_words(input())
print(a)