# lambda arguments : expression

x = lambda a, b: a * b
print(x(5, 6))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# Sum 0f two number

sumTwo = lambda a,b: a+b
print(f'The sum of two number is: ',sumTwo(2,4))



# def function 


