def minimum(arr,n):
    min = arr[0]
    for i in range(1,n):
        if arr [i]<min:
            min=arr[i]
    return min
def maximum(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr [i]>max:
            max=arr[i]
    return max
arr =[8,4,3,9,2]
n=len(arr)
print("largest number is :",maximum(arr,n))
print("smallest number is :",minimum(arr,n))