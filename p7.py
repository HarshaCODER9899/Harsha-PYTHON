"""Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string 
"gnitset ma I"."""

#the time complexity of reverse is O(n)

# the space complexity is O(1)

def reverse(r):
    k=""
    for i in r:
        k=i+k
        
    return k    


print(reverse("i am testing"))
