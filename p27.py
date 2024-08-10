"""Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in
 three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions."""

#the time complexity of by_for_loop is O(N)

# the space complexity is O(1)

def by_for_loop():
    a=['qwerty','asdf','sing','op','456']
    l=[]
    for x in a:
        l.append(len(x))
    return l    

def higher_order_map(x):
    return len(x)
a=['qwerty','asdf','sing','op','456']
b=map(higher_order_map,a)

def list_comp():
    a=['qwerty','asdf','sing','op','456']
    b=[len(x) for x in a]
    return b
print(list_comp())
