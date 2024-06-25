#the time complexity of my_max is O(n)

# the memory usage is 160 bytes



def vowel(v):
    lst=["a","e","i","o","u","A","E","I","O","U"]
    l1=[]
    for x in v:
        if x in lst:
            l1.append("True")
        else:    
         l1.append("False")
    return l1    


print(vowel("asdef"))      
