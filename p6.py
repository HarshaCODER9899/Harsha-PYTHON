def sum(l):
    s=0
    for x in l:
        s+=int(x)
    return s

def multiple(l):
    m=1
    for x in l:
        m*=x
    return m

lst=[]
print("ENTER FOUR NUMBERS")
for i in range(4):
    n=int(input())
    lst.append(n)

print(lst)   
print("sum") 
print(sum(lst))
print("multiple")
print(multiple(lst))    
            