#________OPERATORS___________


#=> Arithmetic operators 

a = 18
b = 4 
print(a + b) #Addition
print(a - b) #Subtraction
print(a * b) #Multiplication
print(a / b) #Division
print(a % b) #Modulus
print(a ** b) #Exponentiation
print(a // b) #Floor division  #  rounds the result down to the nearest whole number

#=> Assignment operators 
c = 12
d = 6
c += d  # a = a + b    
print(c)
c -= d
print(c)
c *= d
print(c)
a /= d
print(c)
a //= d
print(c)
c **= d
print(c)
c %= d
print(c)

## => Comparison Operators

e = 18
f = 9

print(e > f)
print(e >= f)
print(e < f)
print(e <= f)
print(e == f)
print(e != f)

# => Logical Operators

g = 8
h = 23
i = 43

print(g > h and g > i) #Returns True if both statements are true
print (h > i or i > h) #Returns True if one of the statements is true
print(not(True)) #Reverse the result, returns False if the result is true
print(not(False))

#=> Identity Operators
#is:        Returns True if both variables are the same object

# is not:    Returns True if both variables are not the same object
x = 10
y= 10
print (x is y)
print (x is not y)

#=> Membership Operators

#in:        Returns True if a sequence with the specified value is present in the object
#not in:    Returns True if a sequence with the specified value is not present in the object

str = 'iCodeGuru'
print('Code' in str)

print('Code' not in str)
