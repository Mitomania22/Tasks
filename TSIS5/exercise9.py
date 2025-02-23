import re
data="LoveEatingChocolate"
print(re.sub(r"([a-z])([A-Z])", r'\1 \2', data))