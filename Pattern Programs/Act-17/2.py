"""Write a test program that prompts the user to enter a phone number as a string. The input number may 
contain letters. The program translates a letter (uppercase or lowercase) to a digit and leaves all 
other characters intact. Here is a sample run of the program: 
Enter a string: 1-800-Flowers 
1-800-3569377
 Enter a string: 1800flowers 
18003569377 """
pad = ['qz', 'abc', 'def', 'ghi', 'jkl', 'mno', 'prs', 'tuv', 'wxy']
letter_to_numbers = {
    ord(ch): ord(str(i))
    for i, chs in enumerate(pad, 1)
    for ch in chs
}
n=input()
a=n.lower().translate(letter_to_numbers)
print(a)