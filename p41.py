"""In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in 
return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) 
the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play
 Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the
 sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the
 following way:
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]"""

#the time complexity of lingo is O(N)

# the space complexity is O(1)

def lingo():
    t=['t','i','g','e','r']
    word=input("enter a 5 digit word\n")
    g=list(word)
    while len(g)>5 or len(g)<5:
        word=input("enter a 5 digit word\n")
        g=list(word)
        if len(g)==5:
            break
        
    l=list(word)
    T=['[t]','[i]','[g]','[e]','[r]']
    for i in range(0,5):
        if l[i]==t[i]:
            l[i]=T[i]
      
    for i in range(0,5):
        if l[i] in t:
            g="("+l[i]+")"
            l[i]=g
    ans=''
    for i in l:
        ans=ans+i
    return ans        

         
print(lingo())         



        
