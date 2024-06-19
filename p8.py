def is_pal(s):
    for x in range(len(s)):
        k=len(s)-x-1
        if s[x]==s[k]:
            return True
        else:
            return False

print("enter the string to check if it is palandrome")
p=str(input())
print(is_pal(p))        