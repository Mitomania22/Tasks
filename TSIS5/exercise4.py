import re
data="hgedgwgAhedb"
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)