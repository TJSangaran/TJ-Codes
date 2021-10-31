a=input("Enter string one: ")
b=input("Enter string two: ")
a=a.replace(" ","")
b=b.replace(" ","")
l1=list(a.lower())
l2=list(b.lower())
l1.sort()
l2.sort()
if l1==l2:
    print("These are anagrams")
else:
    print("These are not anagrams")
