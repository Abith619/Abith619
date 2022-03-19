"""Craps is a popular dice game played in casinos. Write a program to play a variation of the game, as 
follows: Roll two dice. Each die has six faces representing values 1, 2, …, and 6, respectively. Check 
the sum of the two dice. If the sum is 2, 3, or 12 (called craps), you lose; if the sum is 7 or 11 
(called natural), you win; if the sum is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established. 
Continue to roll the dice until either a 7 or the same point value is rolled. If 7 is rolled, you lose. 
Otherwise, you win. Your program acts as a single player. 
Here are some sample runs. 
You rolled 5 + 6 = 11
 You win 
You rolled 1 + 2 = 3 
You lose 
You rolled 4 + 4 = 8 point is 8
 You rolled 6 + 2 = 8 
You win 
You rolled 3 + 2 = 5 point is 5 
You rolled 2 + 5 = 7 
You lose"""
import random	
import sys

a = input("TO START THE GAME TYPE 'yes' and TO QUIT TYPE 'no'\n")
if a.lower() == "no":
	sys.exit()
else:
	print("LET'S START THE GAME")

def diceNumber():
	_ = input("press enter to roll the dice ")
	die1 = random.randrange(1, 7)
	die2 = random.randrange(1, 7)
	return (die1, die2)

def twoDice(dices):
	die1, die2 = dices
	print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1, die2, sum(dices)))
value = diceNumber()
twoDice(value)

sum_of_dices = sum(value)

if sum_of_dices in (8, 11):
	result = "congratulations you won"
elif sum_of_dices in (5, 3, 7):
	result = "you lost, \ntry again next time"
else:
	result = "continue your game please"
	currentpoint = sum_of_dices
	print("good game, your current point is", currentpoint)

while result == "continue your game please":
	value = diceNumber()
	twoDice(value)
	sum_of_dices = sum(value)
	
	if sum_of_dices == currentpoint:
		result = "congratulations you won"
		
	elif sum_of_dices == 7:
		result = "you lost,\n try again next time"

if result == "congratulations you won":
	print("congratulations,you won")
	
else:
	print("you lost, \ntry again next time")
