import re
data="basbs____jdfe"
matches = re.findall("[a-z]_+[a-z]+", data)
print(matches)