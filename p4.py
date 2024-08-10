"""Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""

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
