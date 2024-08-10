"""Write a program that maps a list of words into a list of integers representing the lengths of the correponding words"""

#the time complexity of lst_of_word_to_int is O(N)

# the space complexity is O(1)

def lst_of_word_to_int():
    words=['qwerty','asdf','sing','op','456']
    int=[]
    for x in words:
        int.append(len(x))
    return int    

print(lst_of_word_to_int())