"""Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a 
member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend 
 Python did not have this operator.)"""

#the time complexity of is_member is O(n)

# the space complexity is O(1)

def is_member(x):
    a=['1','2','3','a','b','asd','qwer']
    i=0
    while i<len(a):
        if x==a[i]:
            return True
        i+=1
    return False    

print(is_member("2"))