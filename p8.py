#the time complexity of my_max is O(n)

# the memory usage is 320 bytes


def is_palindrome(r):
    str=""
    for x in range(len(r)):
        k=len(r)-x-1
        str=str+r[k]
    if r==str:
      return True
    else:
     return False  


print(is_palindrome("radar"))
