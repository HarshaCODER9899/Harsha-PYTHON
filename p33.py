"""According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself
 "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user 
 and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the 
 word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!"""

#the time complexity of semordnilap_recogniser is O(N)

# the space complexity is O(1)

def semordnilap_recognizer():
    f=open("p32readme.txt","r")
    list=[]
    str=""
    for i in f:
        list.append(i)
        str=str+i
    s=str.split()
    
    a=[]
    for i in s:
        b=""
        for j in i: 
           if j!=" " and j!="." and j!="'" and j!="?" and j!="!" and j!=",":
              b=b+j
        c=b.lower()
        a.append(c)  
     
    d=""   
    l=[] 
    for i in a:
        k=''
        for j in i:
            k=j+k
        for x in a:
            if k==x:
                d=i+" "+x
                l.append(d)
    solo=set(l)          
    return solo


print(semordnilap_recognizer())
