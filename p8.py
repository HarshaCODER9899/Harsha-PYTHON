"""Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, 
is_palindrome("radar") should return True."""

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
