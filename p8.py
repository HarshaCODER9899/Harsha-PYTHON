def is_palindrome(r):
    str=""
    for x in range(len(r)):
        k=len(r)-x-1
        str=str+r[k]
    if r==str:
      return True
    else:
     return False  

print("enter string value")
s=str(input())
print(is_palindrome(r=s))
