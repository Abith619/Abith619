# Concatenate two lists in the following order
list1 = ["Hello ", "Good Morning "]
list2 = ["Dear", "Sir"]
con = [i + j for i, j in zip(list1, list2)]
print("HI"+str(con))