def get_string_length(l):
    k=0
    for x in l:
        k+=1
    return k 

print("please input a string")
s=str(input())
print("the length of the given string is")
print(get_string_length(s))
