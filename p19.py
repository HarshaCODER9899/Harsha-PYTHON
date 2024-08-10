""""99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very 
repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Your task
 here is write a Python program capable of generating all the verses of the song."""

#the time complexity of song_99_bottles_of_beer is O(1)

# the space complexity is O(1)

def  Song_99_Bottles_of_Beer():
    i=99
    c=""
    while i>-1:
        j=i-1
        a="\n"+str(i)+" bottles of beer on the wall, "+str(i)+"bottles of beer."
        if j!=-1:
            b="\nTake one down, pass it around,"+str(j)+" bottles of beer on the wall."
            c=c+a+b
        i-=1
    return c    

print(Song_99_Bottles_of_Beer())

