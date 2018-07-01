# move a file to another path

# import os

path = input("Path:\n")
f = open(path, "r")
text = f.read()

newfile = open("f:/"+f.name, 'w')

newfile.write(text)
