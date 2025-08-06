f = open("myfile.txt", "w")  # creates file if not exists, or overwrites if exists
f.write("Hello world!\n")


with open('myfile.txt', 'a') as f:
    f.write("Appending this line.\n")


with open("myfile.txt") as f:
  print(f.read())


with open("myfile.txt", 'a') as f:
   f.write("Successfully understand how to append without overwrite")


with open("myfile.txt") as f:
  print(f.read()) 


f = open("mySecfile.txt", "x") 