import re

s=input()
a=re.findall("[A-Z][a-z]+",s)
for i in range(len(a)):
    print(a[i],end=" ")