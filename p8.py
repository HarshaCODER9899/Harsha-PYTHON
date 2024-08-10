#the time complexity of is_palindrome is O(n)

# the space complexity is O(1)

def is_palindrome(r):
    k=""
    for x in r:
      k=x+k

    if r==k:
      return True
    else:
     return False  


print(is_palindrome("radar"))
