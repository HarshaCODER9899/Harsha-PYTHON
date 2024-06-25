#the time complexity of my_max is O(n)

# the memory usage is 320 bytes


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
       