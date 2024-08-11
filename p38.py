"""Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word 
tokens in the text, divided by the number of word tokens)."""

#the time complexity of average_word_length is O(N)

# the space complexity is O(1)

def average_word_length():
    file=input("ENTER FILE NAME:")
    f=file+".txt"
    o=open(f,"r")
    c=o.read()
    s=c.split("\n",-1)
    
    l=[]
    for i in s:
        j=i.split(" ",-1)
        l=l+j  
    
    list=[]
    for i in l:
        z=1
        for j in i:
            z+=1
        y=z-1    
        list.append(y)
     
    total_no_of_words=len(list)
    p=0
    for i in list:
        p=p+i
    sum_of_words=p
    average_of_words=sum_of_words/total_no_of_words
    return average_of_words    


print(average_word_length())