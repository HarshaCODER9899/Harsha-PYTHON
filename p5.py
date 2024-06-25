#the time complexity of my_max is O(n)

# the memory usage is 160 bytes


def word(w):
    lst=["a","e","i","o","u","A","E","I","O","U"]
    s=""
    for x in w:
        if x in lst:
            s=s+x
        elif x==" ":
            s=s+x      
        else:
            s=s+x+"o"+x
    return s       


print(word("this is fun"))            
