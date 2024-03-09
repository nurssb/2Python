import re

s=input()
s=s.capitalize()
print(re.sub("[ _]","",s))
