# Lists are used to store multiple items in a single variable. 

list1 = [1,2,3,4,5,6]

list2 = [2,4,6,8]

print (list1[2])


# List Operations

#No1: Concatentation Operations


print(list1+list2)

# No2: Repetition Operations
list3 = 'helo '

print(list3 * 5)


#No3 Membership Operations

list4= ['Amna', 'AaMna', 'Fatima', 'Iqra ']
print('AaMna' in list4)

# No4 Slicing Operations

print(list4[1:4])
print(list4[1:2])
print(list4[1:])
print(list4[:])
print(list4[:2])
print(list4[-1:])
print(list4[1::-1]) # reversed 


#--------List Methods----------------

#len() : Returns the length of the list pas as the argument

print(len(list1))

#list(): Create an empty list if no argument is passed.
#list5 =list()

#append(): Appends single element at the end of the list

list6 = ['a', 'b', 'c']
list6.append('d')
print(list6)

#extend(): Appends multiple elements at the end of the list
list7 = ['e','f']

(list6.extend(list7))
print(list6)


# insert():Inserts a new element  at the particular index in the list
list1.insert(0,20)
print(list1)

#count(): Count the number of time a given element in index

list8 = [20, 10, 30, 20, 20, 15,12]
print(list8.count(20))

#index(): First occurence of the element in he list
print('index of ',list8.index(20))

# remove(): Remove the element from the list (first occurence of the element)
(list8.remove(20))
print(list8)

# pop(): remove the element that index is passed as a parameter
print(list8.pop(1))
print(list8)

# if no paramenter is given then remove last element of the list
print(list8.pop())
print(list8)

#Reverse(); Reverse the order of elements in the given list

(list8.reverse())
print(list8)

#Sort(): sorts the elements of given list in place

list8.sort()
print(list8) #ascending order by default


list8.sort(reverse= True) #descending order
print(list8)  

# min (): Return mininum number of list

print(min(list8))

#max (): Return maxinum number of list 
print(max(list8))
#sum(): Return sum of list
print(sum(list8))





