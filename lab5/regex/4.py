import re

s=input()
a=re.search("[A-Z]{1}[a-z]+",s)
if a:
    print("yes")
else:
    print("no")
