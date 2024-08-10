"""Write a function find_longest_word() that takes a list of words and returns the length of the longest one."""

#the time complexity of find_longest_word is O(N)

# the space complexity is O(1)

def find_longest_word():
    a=['qwerty','asdf','sing','4477995','op','456','123456']
    l=[]
    for x in a:
        l.append(len(x))
    
    k=l[0]
    for i in range(len(l)):
        if k<l[i]:
            k=l[i]
        else:
            k==k
    return k        

print(find_longest_word())    