"""Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. 
(Source: http://inventwithpython.com) This is how it should work when run in a terminal:

Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!"""

#the time complexity of guess_the_number is O(N)

# the space complexity is O(1)

def guess_the_number():
    name=input("Hello! What is your name?\n")
    guess=input("Well," +name+", I am thinking of a number between 1 and 20.\nTake a guess.\n")
    
    import random
    r=random.randrange(1, 20)
    guess=int(guess)
    print(r)
    g=0
    while int(guess)!=r:
      if int(guess)>20 or int(guess)<0:
            guess=int(input(name+"Your guess is not in between 1 to 20.\nTake a guess.\n"))
      elif int(guess)>r:
            guess=input("Your guess is too high.\nTake a guess.\n")
            
      elif int(guess)<r:
            guess=int(input("Your guess is too low.\nTake a guess.\n"))
            
      
      g+=1
    g=str(g+1)  
    if guess==r:
         ans= "Good job, " +name+"! You guessed my number in " +g+ " guesses!"       
      
    return ans  
        
print(guess_the_number())        

