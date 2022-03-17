"""In this exercise you will create a Python program that identifies the longest word(s)
in a file. Your program should output an appropriate message that includes the length
of the longest word, along with all of the words of that length that occurred in the
file. Treat any group of non-white space characters as a word, even if it includes
numbers or punctuation marks"""

def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    print(max_len)
    return [word for word in words if len(word) == max_len]
print(longest_words('124.txt'))