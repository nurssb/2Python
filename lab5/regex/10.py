import re

s=input()
s=re.sub("([a-z]$)",r"\1.",s)
print(re.sub("([A-Z][a-z]+)",r"\1_",s).lower())