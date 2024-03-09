import re

s=input()
result=re.search("^a""[b]{2,3}",s)

if result:
    print("yes")
else:
    print("no")