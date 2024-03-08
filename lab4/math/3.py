import math

n=int(input("Input number of sides: "))
leng=int(input("Input the length of a side: "))
r=leng/(2*(math.tan(180/n)))
print(((n*leng)*r)/2)