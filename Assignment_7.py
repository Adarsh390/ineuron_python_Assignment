#Problem 1: Program to Print Sum of array
#Sol:
array = list(map(int,input().strip().split()))
s = 0
for i in array:
    s+=i
print("Sum of Array: ",s)

#Problem 2: Program to find largest element in an array
arr = list(map(int,input().strip().split()))
le = arr[0]
for i in range(1,len(arr)):
    if(arr[i]>le):
        le = arr[i]
print(le)

#Problem 3: Program to rotate an array
arr = list(map(int,input().strip().split()))
print(arr[::-1])

#Problem 4: Program to split the array and add the first part ot end 
#Sol:
def splitAdd(l, split):
    out = []
    for i in range(len(l)):
        index = (i+len(l)+split)%len(l)
        out.append(l[index])
        
    return out

#Problem 5: Program to chech given array is monotonic
#sol:
def monotonicCheck(array):
    flag = True
    
    if array[0] >= array[len(array)-1]:
        for i in range(len(array)-2):
            if array[i] < array[i+1]:
                flag = False
    else:
        for i in range(len(array)-2):
            if array[i] > array[i+1]:
                flag = False
                
    return flag

