"""An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using 
all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that,
 when started 1) randomly picks a word w from given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents
 the anagram to the user, and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good
 idea to work with (say) colour words only. The interaction with the program may look like so:
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!"""

#the time complexity of translate is O(N)

# the space complexity is O(1)

def word_play():
    import random
    r=random.randrange(0, 11)
    
    colour=["red","blue","black","brown","yellow","orange","green","purple","gray","white","pink"]
    c=list(colour[r])
    random.shuffle(c)
    
    w=""
    x="correct!"
    for i in c:
        w=w+i
    print("Colour word anagram: "+w)
    inp=input("Guess the colour word!")
    while inp!=colour[r]:
       if inp==colour[r]:
           break
       inp=input("Guess the colour word!")    
    return x   


print(word_play())    
    