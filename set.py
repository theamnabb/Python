# A set is a collection which is unordered, unchangeable*, and unindexed.

#Sets are written with curly brackets.

set1 = {"apple", "banana", "cherry"}
print(set1)

# methods
#add()
set1.add("Mango")

print(set1)

#pop()

set1.pop()
print('pop',set1)

#remove()

#set1.remove("cherry")
print(set1)

#clear()

set1.clear()
print(set1)

#union()

set2 = {1,3,5,7,9}
set3= {2,4,6,8,10}
set4= set2.union(set3)
print(set4)
