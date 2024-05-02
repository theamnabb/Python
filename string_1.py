# --------- String built in function --------

# Len() : returns the length of String

a = ' We learn Built-in-function for string'
print ('Length of a:', len(a))

# upper() :returns the string in upper case

print(a.upper())

# lower() :returns the string in lower case

print(a.lower())

#islower()	Returns True if all characters in the string are lower case

print(a.islower())

#strip():  method removes any whitespace from the beginning or the end

print(a.strip())

# replace(): method replaces a string with another string

print(a.replace("string", "String"))

#split(): method returns a list where the text between the specified separator becomes the list items.

b = 'Helo,World'
print(b.split(','))

#title():   Converts the first character of each word to upper case

print(a.title())

# count():  Returns the number of times a specified value occurs in a string

print(a.count('n'))

#find()	Searches the string for a specified value and returns the position of where it was found

print(a.find('n'))

# index():   Searches the string for a specified value and returns the position of where it was found

print(a.index('n'))

#endswith():    Returns true if the string ends with the specified value

print(a.endswith('g'))

#startswith():  method returns True if the string starts with the specified value, otherwise False.

print(a.startswith('b'))

#join():    Converts the elements of an iterable into a string

print('-'.join(a))

#partition():   Returns a tuple where the string is parted into three parts

print(a.partition('Built-in-function'))




