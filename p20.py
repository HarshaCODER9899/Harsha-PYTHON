"""Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", 
"happy":"gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. That is, write a
 function translate() that takes a list of English words and returns a list of Swedish words."""

#the time complexity of translate_swidish_from_english is O(N)

# the space complexity is O(1)

def translate_swidish_from_english(e):
    swidict={"merry":"god", "christmas":"jul","and":"och","happy":"gott", "new":"nytt", "year":"år"}
    english=e
    lst=english.split(" ")
    swedish=""
    for i in lst:
        word=swidict[i]
        swedish=swedish+" "+word
    return swedish
 

print(translate_swidish_from_english("merry christmas and happy christmas"))    

