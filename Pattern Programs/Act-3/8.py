# Counts the number of occurrences of all the items from a given tuple
from collections import Counter
tup = [50, 10, 60, 70, 50,80,90,50,60,70,50,70]
c = Counter(tup)
print(c)