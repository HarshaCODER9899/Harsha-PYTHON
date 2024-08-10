"""Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or more occurrences of the
 space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter.
   E.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use regular 
   expressions!"""

#the time complexity of spelling_correction is O(N)

# the space complexity is O(1)

def spelling_correction(s):
    a=s
    b=""
    d=""
    c=a.split(" ")

    for i in c:
        if i!="":
            d=d+" "+i

    e=""
    for i in d:
        if i==".":
            i=i+" "
        b=b+i
    b=b.split(".")
    
    for i in b:
        if i!="":
          i.strip()
          e=e+i+"."

    return e

print(spelling_correction("This is    very funny    and  cool. Indeed!"))
