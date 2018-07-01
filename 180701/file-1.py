# file test:
# open a file

path = input("please input a file path:\n")
f = open(path, "r")
print(f.read())
