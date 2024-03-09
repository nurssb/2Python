import os

path = r'C:\Users\acer\Documents\sss\lab6\dir-and-files\text.txt'

with open(path, 'r') as f:
	lines = len(f.readlines())
	print(lines)