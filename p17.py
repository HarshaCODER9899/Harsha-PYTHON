"""Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was 
it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I
 roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, 
 capitalization, and spacing are usually ignored"""

#the time complexity of palindrome_recog is O(N+M)

# the space complexity is O(1)

def palindrome_recog(x):
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
      return True
    else:
     return False  

print(palindrome_recog("Was it a rat I saw?"))