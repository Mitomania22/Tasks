import re
data="abbaac"
matches = re.findall("a.*b", data)
print(matches)