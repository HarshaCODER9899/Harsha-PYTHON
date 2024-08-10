#the time complexity of reverse is O(n)

# the space complexity is O(1)

def reverse(r):
    k=""
    for i in r:
        k=i+k
        
    return k    


print(reverse("i am testing"))
