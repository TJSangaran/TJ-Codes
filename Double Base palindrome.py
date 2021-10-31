s=input("Enter Input: ")
if int(s) in range(1,10):
    print("Yes")
else:
    n=0
    l=len(s)-1
    while n<l:
        if s[n]==s[l]:
            n+=1
            l-=1
        else:
            print("No")
            break
    if n>=l:
        print("Yes")
