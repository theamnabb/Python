#Tuples
#A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.


t = (3,4,5,6,7,8,9,6,11,6,13)
print(t)
#Methods

#count()
print(t.count(6))

#index()
print(t.index(4))

#len()
print(len(t))


#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
