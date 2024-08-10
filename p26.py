"""Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one.
 Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?"""

#the time complexity of max_in_list is O(N)

# the space complexity is O(1)

def max_in_list(*x):
    lst=list(x)
    import functools
    return functools.reduce(lambda a,b: a if a > b else b, lst)

print(max_in_list(2,3,4,9,8,6,7))


