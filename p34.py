"""Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of
 the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen."""

#the time complexity of char_freq_table is O(N²)

# the space complexity is O(1)

def char_freq_table():
    file=input("ENTER FILE NAME:")
    f=file+".txt"
    o=open(f,"r")
    c=o.read()
    mydict={}
    d=set(c)
    
    for i in d:
        e=0
        for j in c:
            if i==j:
                e+=1
        mydict[i]=e
    myKeys = list(mydict.keys())
    myKeys.sort()
    sorted_dict = {i: mydict[i] for i in myKeys}
    return sorted_dict    
                
    



print(char_freq_table())
   
