import numpy as np

def LetterCapitalize(str):
    word = str.split()
    newstring = ""

    for i in word:
        newstring += i.title() + " "
    print(newstring)

def SimpleAdding(num):
    num = 10
    sum = 0

    for i in range(1, num+1):
        sum += i
    print(sum)
    SimpleAdding(input(int(num)))

s="HTIBA"
def reverse_string(s):
    return s[::-1]

def FirstFactorial(num):
    sum = 1
    count = 1
    while count <= num:
        sum = sum * count
        count += 1
    print(sum)

def longestword(sen):
    test=str.split()
    greatest=test[0]

    for word in test:
       if len(test)>len(greatest):
           greatest = word
    print(greatest)

def LetterChanges(str):
    lower = str.lower()
    newstring = ""
    lookup = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"

    for letter in lower:
        if letter == "z":
            newstring += "A"
        else:
            letter_index = lookup.index(letter)
            if lookup[(letter_index+1)] in vowels:
                vowel_set = lookup[(letter_index+1)]
                newstring += vowel_set.upper()
            else:
                newstring += lookup[(letter_index+1)]
    print (newstring)

LetterChanges(str="hello world")
print(reverse_string("OlleH "+s))

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))

list=[1,2,3,4,5]
rev=list[::-1]
print(rev)
rev_list=[]

for item in rev:
    rev_list.append(item)
print(rev_list)


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
class interview():
    list=[1,2,3,4,5]
    set = {1,2,3,4,5}
    tuple = (1,2,3,4,5)
    dict = {"name":"Rahul","age":25,"city":"Delhi"}

    def data_structure(self):
        arr = np.array([1, 2, 3])
        print("Array with Rank 1: \n",arr)
        sliced_arr = arr[:2, ::2]

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2f}")
