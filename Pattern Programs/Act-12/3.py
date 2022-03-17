"""Write a program that displays the word (or words) that occur most frequently in a file. Your 
program should begin by reading the name of the file from the user. Then it should find the 
word(s) by splitting each line in the file at each space. Finally,any leading or trailing 
punctuation marks should be removed from each word. In addition, your program should ignore 
capitalization. As a result, apple, apple!, Apple and ApPlE should all be treated as the same 
word. You will probably find your solution to Exercise 111 helpful when completing this problem"""
file=open("123.txt", "r")
frequent_word = ""
frequency = 0 
words = []
for line in file:
    line_word = line.lower().replace(',','').replace('.','').split(" ");
    for w in line_word: 
        words.append(w);
for i in range(0, len(words)):
    count = 1; 
    for j in range(i+1, len(words)): 
        if(words[i] == words[j]): 
            count = count + 1; 
    if(count > frequency): 
        frequency = count; 
        frequent_word = words[i];
print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))
file.close(); 