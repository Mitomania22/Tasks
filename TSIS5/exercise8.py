import re
data="ILoveEatingChocolate"
print(re.findall(r"[A-Z][^A-Z]*", data))