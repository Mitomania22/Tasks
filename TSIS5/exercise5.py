import re
data="ab_aabababbabaABcdcbdb"
matches = re.findall(r"a+.b", data)
print(matches)