"""The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers,
 respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a 
 function max_in_list() that takes a list of numbers and returns the largest one."""

#the time complexity of max_in_list is O(N)

# the space complexity is O(1)

def max_in_list(*x):
    l=list(x)

    k=l[0]
    for i in range(len(l)):
        if k<l[i]:
            k=l[i]
        else:
            k==k
    return k            
        

print(max_in_list(2,3,9,5,7,6,13))           
