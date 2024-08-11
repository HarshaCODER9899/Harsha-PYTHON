"""Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 
1 to n (where n is the number of lines in the file)."""

#the time complexity of number_file is O(N)

# the space complexity is O(1)

def number_file():
    file=input("ENTER FILE NAME:")
    f=file+".txt"
    o=open(f,"r")
   
    list=[]
    for i in o:
        list.append(i)
   
    j=1
    lst= []
    for i in list:
        lst.append(j)
        j+=1

    s=""
    for i in lst:
        j=str(i)
        s=s+j+"\n"
    print("NEW FILE NAME:myfile")
    g=open("myfile.txt","w")
    g.write(s)
    g.close()
    g=open("myfile.txt","r")
    return g.read()



print(number_file())
