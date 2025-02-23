import re
data="ILoveEatingChocolate"
matches=re.sub(r'(?<!^)(?=[A-Z])', '_', data).lower()
print(matches)