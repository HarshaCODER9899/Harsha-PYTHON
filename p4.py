def vowel(v):
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
    for x in v:
        if x==a or x==e or x==i or x==o or x==u or x==A or x==E or x==I or x==O or x==U:
            print("true") 
        else:
            print(False)

print("please input a char or string")
s=str(input())
print("vowel be return as true")
print(vowel(s))        