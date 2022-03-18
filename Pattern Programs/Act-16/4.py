"""Write a program that prompts the user to enter two strings and reports whether the second string is a 
substring of the first string. Enter string s1: ABCD 
Enter string s2: BC
 BC is a substring of ABCD 
 Enter string s1: ABCD
 Enter string s2: BDC 
BDC is not a substring of ABCD"""
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
string = "ABCD"
sub_str ="AB"
check(string, sub_str)