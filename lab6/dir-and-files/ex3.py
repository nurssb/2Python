import os

path = r'C:\Users\acer\Documents\sss\lab6\dir-and-files\text.txt'
if os.access(path, os.F_OK):
     print("\n" + os.path.basename(path))
     print("\n" + os.path.dirname(path) + "\n")
else:
     print(f"{path} do not exists")