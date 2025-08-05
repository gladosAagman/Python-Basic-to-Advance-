lst = [4,3,2,1,2]
n = len(lst)
smallest=1000
smallest_index=-1
for i in range(0,n):
    if lst[i] < smallest:
        smallest = lst[i]
        smallest_index = i 

print("Smallest is %d located at %d "%(smallest,smallest_index))