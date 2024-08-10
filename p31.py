"""Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good 
exercise.)"""
#the time complexity of translate is O(N)

# the space complexity is O(1)
def my_map(x,y):
    k=[]
    for i in y:
        k.append(x(i))
        
        return x    
      
def func(i):
    i=len(i)
    return i
y=['qwerty','asdf','sing','op']
print(map(func,y))
lst=list(map(func,y))
print(lst)


print(my_map(func,y))
l1=list(my_map(func,y))
print(l1)
