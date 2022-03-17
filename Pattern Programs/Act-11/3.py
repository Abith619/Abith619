"""Use the Account class created in Programming Exercise 9.7 to simulate an ATM machine. Create 
ten accounts in an array with id-0 , 1 , . . . , 9 , and initial balance $100. The system prompts
the user to enter an id. If the id is entered incorrectly, ask the user to enter a correct id.
Once an id is accepted, the main menu is displayed as shown in the sample run. You can enter 
a choice 1 for viewing the current balance, 2 for withdrawing money, 3 for depositing money, 
and 4 for exiting the main menu. Once you exit, the system will prompt for an id again. Thus, 
once the system starts, it will not stop.
	•	Enter an id: 4
	•	Main menu
	•	1: check balance
	•	2: withdraw
	•	3: deposit
	•	4: exit
	•	Enter a choice: 1
	•	The balance is 100.0
	•	Main menu
	•	1: check balance
	•	2: withdraw
	•	3: deposit
	•	4: exit
	•	Enter a choice: 2
	•	Enter an amount to withdraw: 3
	•	Main menu
	•	1: check balance
	•	2: withdraw
	•	3: deposit
	•	4: exit
	•	Enter a choice: 1
	•	The balance is 97.0
	•	Main menu
	•	1: check balance
	•	2: withdraw
	•	3: deposit
	•	4: exit
	•	Enter a choice: 3
	•	Enter an amount to deposit: 10
	•	Main menu
	•	1: check balance
	•	2: withdraw
	•	3: deposit
	•	4: exit
	•	Enter a choice: 1
	•	The balance is 107.0
	•	Main menu
	•	1: check balance
	•	2: withdraw
	•	3: deposit
	•	4: exit
	•	Enter a choice: 4
	•	Enter an id:"""
from numpy import array
import random
import sys
class Account():
    def __init__(self, name, account_number=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), balance = 100):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance is : ", self.balance)
        print()
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"RS:{amount} withdrawal successful!")
            print("Current account balance : ", self.balance)
            print()
    def check_balance(self):
        print("Available balance= ", self.balance)
        print()
    def transaction(self):
        print("""
            Main-Menu:
            1. Check Balance
            2. Deposit
            3. Withdraw
            4. Exit""")
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 : "))
            except:
                print("Error: Enter 1, 2, 3, 4 only!\n")
                continue
            else:
                if option == 1:
                    account.check_balance()
                elif option == 2:
                    amount = int(input("Enter Amount you want to deposit : "))
                    account.deposit(amount)
                elif option == 3:
                    amount = int(input("Enter Amount you want to withdraw : "))
                    account.withdraw(amount)
                elif option == 4:
                    print(f"""                         
              Transaction number: {random.randint(100, 999)}
              Account ID: {self.name}
              Available balance = RS.{self.balance}""")
                    sys.exit()
print("Welcome to ATM")
account_number = [input("Enter your ID: ")]
account = Account(account_number)
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        account.transaction()
    elif trans == "n":
        print("""Bye""")
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")