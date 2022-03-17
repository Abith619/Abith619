"""Write a Python function that takes two lists and returns True if they have at least one 
common member"""
def compareList(l1,l2):
   if(l1==l2):
      return "Equal"
   else:
      return "Not equal"
l1=[1,2,3]
l2=[2,1,3]
print("First list",compareList(l1,l2))
l3=[1,2,3]
l4=[1,2,3]
print("Second list",compareList(l3,l4))