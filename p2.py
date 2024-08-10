#the time complexity of my_max is O(n)
# the space complexity is O(1)


def my_max(x,y,z):
    if x>y>z or x>z>y:
        return x
    elif y>x>z or y>z>x:
        return y
    else:
        return z


print(my_max(4,3,2))


