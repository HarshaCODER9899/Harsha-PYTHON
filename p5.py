"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every
 consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string 
 "tothohisos isos fofunon"."""

#the time complexity of my_max is O(n)

# the space complexity is O(1)


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
