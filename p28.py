"""Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order 
functions."""

#the time complexity of find_longest_word is O(N)

# the space complexity is O(1)

def find_longest_word():
    a=['qwerty','asdf','sing','1234567','op','456']
    b=map(lambda i:len(i),a)
    lst=list(b)
    import functools
    return functools.reduce(lambda a,b: a if a > b else b, lst)

 
print(find_longest_word())