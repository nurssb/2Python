import re

s=input()
result=re.search("^a""b*$",s)

if result:
    print("yes")
else:
    print("no")