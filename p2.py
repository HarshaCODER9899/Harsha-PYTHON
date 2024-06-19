def mymax(x,y,z):
    if x>y>z or x>z>y:
        return x
    elif y>x>z or y>z>x:
        return y
    else:
        return z

print("enter first number")    
a=int(input())    
print("enter another number") 
b=int(input())
print("enter another number please") 
c=int(input())
print("the largest of them is ")
print(mymax(x=a,y=b,z=c))
quit()