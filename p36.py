"""A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the 
works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure
 your program ignores capitalization."""

def hapax_legomenon():
    file=input("ENTER FILE NAME:")
    f=file+".txt"
    o=open(f,"r")    
    list=[]
    str=""
    for i in o:
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
    print(a) 
    dict={} 
    for i in a:
        c=0
        for j in range(len(a)):
           if i==a[j]:
              c+=1
        dict[i]=c
    print(dict)
    h=[]
    for i in dict.keys():
        if dict[i]==1:
            h.append(i)
    print(h)

print(hapax_legomenon())    