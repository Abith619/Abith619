# Write a Python script to merge two Python dictionaries.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
def merge(dic1, dic2):
    return (dic2.update(dic1))
print(merge(dic1, dic2))
print(dic2)