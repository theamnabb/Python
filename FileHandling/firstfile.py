f = open("myfile.txt", "w")  # creates file if not exists, or overwrites if exists
f.write("Hello world!")


with open('myfile.txt', 'a') as f:
    f.write("Appending this line.\n")