import re
data="ab_aabababbaba"
matches = re.findall("a.*bb+|abbb+", data)
print(matches)