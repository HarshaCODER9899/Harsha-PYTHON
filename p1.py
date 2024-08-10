"""Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available 
in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)"""

#the time complexity of my_max is O(1)
# the space complexity is O(1)


def my_max(x,y):
    if x>y:
        return x
    else:
        return y


print( my_max(5,6))
