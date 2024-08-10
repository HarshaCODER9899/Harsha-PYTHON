"""Write a function find_longest_word() that takes a list of words and returns the length of the longest one."""

#the time complexity of find_longest_word is O(N)

# the space complexity is O(1)

def find_longest_word():
    words=['qwerty','asdf','sing','4..477995','op','456','123456']
    lst=[]
    for i in words:
        lst.append(len(i))
    
    longest=lst[0]
    for i in range(len(lst)):
        if longest<lst[i]:
            longest=lst[i]
        else:
            longest==longest
    return longest        

print(find_longest_word())    