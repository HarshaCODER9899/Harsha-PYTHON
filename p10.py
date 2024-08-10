""" Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. 
You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested
 for-loops"""

#the time complexity of overlapping is O(N²)

# the space complexity is O(1)

def overlapping(x):
    a=['1','2','4','a','z','w']
    b=['3','5','b']
    b.append(x)
    for i in a:
        for j in b:
            if i==j:
                return True
    return False        

print(overlapping('15'))