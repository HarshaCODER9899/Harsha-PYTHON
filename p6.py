"""Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For
 example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""

#the time complexity of sum is O(n) and of multiple is O(m)

# the space complexity is o(m+n)


def sum(*l):
    s=0
    for x in l:
        s+=int(x)
    return s

def multiple(*l):
    m=1
    for x in l:
        m*=x
    return m


print(sum(1,2,3,4))

print(multiple(1,2,3,4))    
       