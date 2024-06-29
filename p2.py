#the time complexity of max_of_three is O(n^3)

# the memory usage is 160 bytes


def max_of_three(a,b,c):
    l=[a,b,c]
    s=0
    for x in l:
        for y in l:
            for z in l:
                x!=y!=z
                if x>y>z:
                    return x
            
        
print(max_of_three(6,7,9))       
