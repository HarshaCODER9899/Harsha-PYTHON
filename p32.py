"""Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the 
screen if it is a palindrome"""

#the time complexity of palindrome_recogniser is O(NM)

# the space complexity is O(1)

def palindrome_recogniser():
    f=open("p32readme.txt","r")
    str=""
    for i in f:
        str=str+i
    s=str.split("\n",-1)
    c=""
    for x in s:
        a=x
        b=""
        for j in a: 
           if j!=" " and j!="." and j!="'" and j!="?" and j!="!" and j!=",":
              b=b+j
        b=b.lower()   
        str=""
        for i in range(len(b)):
           k=len(b)-i-1
           str=str+b[k]
        if b==str:
           c=c+a
           return True
        else:
            False
           
         
    return c       
        
        

print(palindrome_recogniser())    