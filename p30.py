"""Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och",
 "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Use the higher order
function map() to write a function translate() that takes a list of English words and returns a list of Swedish words."""

#the time complexity of translate is O(N)

# the space complexity is O(1)

def translate(x):
    x=x.split(" ")
    a= {"merry":"god", "christmas":"jul", "and":"och","happy":"gott", "new":"nytt", "year":"år"} 
    b=map(lambda i:a[i],x)
    c=list(b)
    d=""
    for i in c:
        d=d+" "+i
    return d  


print(translate("merry christmas and new year"))