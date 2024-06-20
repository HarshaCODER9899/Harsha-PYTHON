def reverse(r):
    str=""
    for x in range(len(s)):
        k=len(s)-x-1
        str=str+s[k]
    print(str)    

print("enter string value")
s=str(input())
print(reverse(r=s))
