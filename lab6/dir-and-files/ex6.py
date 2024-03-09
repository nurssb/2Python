import os

path = r"C:\Users\acer\Documents\sss\lab6\folder"

for i in range(65,91):
    name = os.path.join(path, chr(i) + ".txt")
    f = open(name, "a")