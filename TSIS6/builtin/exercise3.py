def palindrom(s,palind):
    for i in s:
        for j in palind:
            if i!=j:
                return False
                break
            return True
        
    

s=str(input("enter sentence:"))
palind=''.join(reversed(s))
print(palindrom(s,palind))