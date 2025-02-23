import re
data="ABCDEF,GHabc,def.gh"
matches=re.sub(r"[., ]",':',data)
print(matches)