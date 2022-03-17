"""Write two functions, hex2int and int2hex, that convert between hexadecimal
digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and base 10 integers. The
hex2int function is responsible for converting a string containing a single hexadec-
imal digit to a base 10 integer, while the int2hex function is responsible for con-
verting an integer between 0 and 15 to a single hexadecimal digit. Each function will
take the value to convert as its only parameter and return the converted value as the
function's only result. Ensure that the hex2int function works correctly for both
uppercase and lowercase letters. Your functions should end the program with a
meaningful error message if an invalid parameter is provided."""

int2hex=hex(11)
print(int2hex)

hex2int=int("B", 16)
print(hex2int)
"""def hexadecimalToDecimal(hexval):
    length = len(hexval)
    base = int(input("Enter a value:"))
    dec_val = int(input("Enter a number:"))
 
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val
if __name__ == '__main__':
    hexnum = '1A'
    print(hexadecimalToDecimal(hexnum))
else:
    print("The value entered id INVALID !")"""