"""Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but
 writing it yourself is nevertheless a good exercise.)"""

#the time complexity is O(n)

# the space complexity is O(1)


def length_of_the_string(l):
    k=0
    for x in l:
        k+=1
    return k 


print(length_of_the_string("asdfg"))
