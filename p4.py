#the time complexity of checking_vowel is O(n)

# the memory usage is 160 bytes



def checking_vowel(v):
    #gives true for an vowel and false for a consolent
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    l1=[]
    for x in v:
        if x in vowels:
            l1.append("True")
        else:    
         l1.append("False")
    return l1    


print(checking_vowel("asdef"))      
