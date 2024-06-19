def mymax(x,y):
    if x>y:
        return x
    else:
        return y

print("enter first number")    
a=int(input())    
print("enter another number") 
b=int(input())
print("the largest of them is ")
print(mymax(x=a,y=b))
