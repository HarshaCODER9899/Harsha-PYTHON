"""Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n"""
#the time complexity of filter_long_words is O(N)

# the space complexity is O(1)

def filter_long_words():
    lst_of_words=['qwerty','asdf','sing','4477995','op','456','123456']
    n=4
    l=[]
    for i in lst_of_words:
        if len(i)>n:
            l.append(i)
    return l

print(filter_long_words())        



