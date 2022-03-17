"""(Longest common prefix) Write a program that prompts the user to enter two
strings and displays the largest common prefix of the two strings. Here are some sample runs:

Enter the first string: Welcome to C++
Enter the second string: Welcome to programming
The common prefix is Welcome to

Enter the first string: Atlanta
Enter the second string: Macon
Atlanta and Macon have no common prefix"""
def commonPrefixUtil(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    result = ""
    j = 0
    i = 0
    while(i <= n1 - 1 and j <= n2 - 1):
        if (str1[i] != str2[j]):
            break
        result += (str1[i])
        i += 1
        j += 1
    return (result)
def commonPrefix(a, n):
    a.sort(reverse = False)
    print(commonPrefixUtil(a[0], a[n - 1]))
if __name__ == '__main__':
    a = [input(), input()]
    n = len(a)
    commonPrefix(a, n)