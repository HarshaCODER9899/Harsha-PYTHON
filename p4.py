#the time complexity of checking_vowel is O(n)

# the space complexity is O(1)



def checking_vowel(v):
    #gives true for an vowel and false for a consolent
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    
    for x in v:
        if x in vowels:
            return True
        else:
            return False    
        
  


print(checking_vowel("k"))      
