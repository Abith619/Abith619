""" Many people think about their height in feet and inches, even in some countries that 
primarily use the metric system. Write a program that reads a number of feet from the user, 
followed by a number of inches. Once these values are read, your program should compute and 
display the equivalent number of centimeters.Hint: One foot is 12 inches. One inch is 2.54 centimeters"""
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %d cm." % h_cm)