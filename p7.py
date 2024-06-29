#the time complexity of my_max is O(n)

# the memory usage is 160 bytes

def reverse(r):
    str=""
    for x in range(len(r)):
        k=len(r)-x-1
        str=str+r[k]
    return str    


print(reverse("harsha"))
