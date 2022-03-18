"""In this exercise you will write a function that determines whether or not a password is good. 
We will define a good password to be a one that is at least 8 characters long and contains at 
least one uppercase letter, at least one lowercase letter, and at least one number. Your function 
should return true if the password passed to it as its only parameter is good. Otherwise it should 
return false. Include a main program that reads a password from the user and reports whether or 
not it is good. Ensure that your main program only runs when your solution has not been imported 
into another file"""
l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
if (len(s) >= 8):
	for i in s:
		if (i.islower()):
			l+=1			
		if (i.isupper()):
			u+=1			
		if (i.isdigit()):
			d+=1			
		if(i=='@'or i=='$' or i=='_'):
			p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")