"""Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the
 frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")."""

#the time complexity of char_freq is O(N)

# the space complexity is O(1)  

def char_freq(c):
    mydict={}
    a=c
    d=set(a)
    for i in d:
        e=0
        for j in a:
            if i==j:
               e+=1
        mydict[i]=e 
    return mydict      


print(char_freq("abbabcbdba.#$Fbdbdbabababcbcbab"))    
