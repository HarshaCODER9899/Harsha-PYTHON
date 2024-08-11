"""Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and 
returns the list of words that are longer than n."""

#the time complexity of filter_long_words is O(N)

# the space complexity is O(1)

def filter_long_words(x):
    return len(x)>5

a=['qwerty','asdf','sing','1234567','op','456']
c=list(filter(filter_long_words,a))
print(c)