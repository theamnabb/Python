#_______________Assignment_02________________

# _____________String Handling_______________

#QNo1 : Write a program to find length of a string.

str1 = 'MaHaGul'
print('Length of Str1 is:',len(str1))


#QNo2: Write a program to copy one string to another string.

# using simple assignment
str1 = 'MaHaGul'
str2 = str1
print('Copy String by using Simple Assignment:',str2)

#-----------OR----------------


#using slicing method
str2 = str1[:]
print('By using Slicing method:',str2)


#QNo3: Write a program to concatenate two strings.

print('Concatenate two string:',str1 + ' ' + str2)


#Qno4: Write a program to compare two strings. 
str1 = 'MaHaGul'
str3 = 'GulMaHa'

result = str1 == str3
print('Output of Compare String:', result)


#Qno5: Write a program to convert lowercase string to uppercase.
str3 = 'GulMaHa'
print('Lower to Upper:',str3.upper())


#Qno6:Write a program to convert uppercase string to lowercase.
str3 = 'GulMaHa'
print('Upper to Lower:',str3.lower())




#Qno14: Write a program to find first occurrence of a character in a given string.

print('First Occurrence:',str3.index('a'))


#Qno15: Write a program to find last occurrence of a character in a given string.

print('Last Occurrence:',str3.rindex('a'))


#Qno16: Write a program to search all occurrences of a character in given string.

str5 = 'I\'m here for practising the methods of string'
user = input('Enter a Charachter: ')
allOccurrs = []

for i in range(len(str5)):
 if (str5[i] == user):
     allOccurrs.append(i)

if allOccurrs:
    print(f"The character {user} occurs at the following indices in {str5}: {allOccurrs}")
else:
    print(f"The character {user} is not found in {str5}.")


#Qno17: Write a program to count occurrences of a character in given string.

str5 = 'methods of string'
user = input('Enter a Charachter: ')
allOccurrs = 0

for i in range(len(str5)):
 if (str5[i] == user):
     allOccurrs += 1

if allOccurrs:
    print(f"The character '{user}' occurs {allOccurrs} times in '{str5}'.")
else:
    print(f"The character '{user}' is not found in '{str5}'.")


#Qno21: Write a program to remove first occurrence of a character from string.

