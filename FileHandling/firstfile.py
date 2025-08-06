f = open("myfile.txt", "w")  # creates file if not exists, or overwrites if exists
f.write("Hello world!\n")


with open('myfile.txt', 'a') as f:
    f.write("Appending this line.\n")


with open("demofile.txt") as f:
  print(f.read())