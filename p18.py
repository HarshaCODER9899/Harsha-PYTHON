"""A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
 The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram 
 or not"""

#the time complexity of check_pangram is O(N)

# the space complexity is O(1)

def check_pangram(x):
    set_of_alphabets={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    a=x
    b=""
    for j in a: 
       if j!=" " and j!="." and j!="'" and j!="?" and j!="!" and j!=",":
          b=b+j
    b=b.lower() 
    c=set(b)
    if c==set_of_alphabets:
       return True
    else:
       return False

print(check_pangram("The quick brown fox jumps over the lazy dog"))
