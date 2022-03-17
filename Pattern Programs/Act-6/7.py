"""7)Write a Python program to check all values are same in a dictionary.
Original Dictionary:
{&#39;Cierra Vega&#39;: 12, &#39;Alden Cantrell&#39;: 12, &#39;Kierra Gentry&#39;: 12, &#39;Pierre Cox&#39;:12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.
False"""
dictionary={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox':13}


def value_check(dictionary, n):
    result = all(x == n for x in dictionary.values()) 
    return result

n = int(input("Enter a number:"))
print("\nCheck all are ",n,"in the dictionary.")
print(value_check(dictionary, n))

n = int(input("Enter a number:"))
print("\nCheck all are ",n,"in the dictionary.")
print(value_check(dictionary, n))