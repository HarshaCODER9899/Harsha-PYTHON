def my_max(x,y):
    if x>y:
        return x
    else:
        return y

print("enter first number")    
a=int(input())    
print("enter another number") 
b=int(input())
print("the largest of them is ")
print(my_max(x=a,y=b))
