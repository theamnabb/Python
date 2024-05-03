#Contiotonal Statement

#=> if statement 

age = int(input('Enter Your Age:'))
if age>18:
    print('You can apply')


#if else

age = int(input('Enter Your Age:'))
if age>18:
    print('You can apply')
else:
    print('You can\'t apply')

#if elif ....... statements

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#short hand

a = 2
b = 330 
print("A") if a > b else print("B")

#Nested if

age = 17
own_car = 'false'

#outer if statement

if (age >= 18):
   #inner if statement
   if (own_car == 'true'):
      print('Drive your car')
    #inner else statement
   else:
      print('Work hard')
# outer if statement
else:
   print('Drive after 18')


