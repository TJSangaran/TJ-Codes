s=input()
t=""
vowels=["a","e","i","o","u","A","E","I","O","U"]
for i in s:
    if i in vowels or not(i.isalpha()):
        t=t+i
    else:
        t=t+i+"o"+i.lower()
print(t)
