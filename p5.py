def word(w):
    a="a"
    e="e"
    i="i"
    o="o"
    u="u"
    A="A"
    E="E"
    I="I"
    O="O"
    U="U"
    s=" "
    for x in w:
        if x==a or x==e or x==i or x==o or x==u or x==A or x==E or x==I or x==O or x==U:
            s=s+x
        elif x==" ":
            s=s+x      
        else:
            s=s+x+"o"+x
    print(s)        

print("please input a char or string")
r=str(input())
print("the given input is converted as")
print(word(r))            
