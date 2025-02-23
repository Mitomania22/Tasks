import re
data="Bcc_aajAjD_jajaa_Arr"
matches=re.sub(r"_",'',data)
print(matches)