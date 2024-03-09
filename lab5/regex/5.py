import re

s=input()
a=re.search(".*a+.*b$",s)

if a:
    print("yes")
else:
    print("no")

