# Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ab"] 
list2 = ["y", "me", "s", "ith"]

con = [i + j for i, j in zip(list1, list2)]

print ("The list element concatenation is : " + str(con))

