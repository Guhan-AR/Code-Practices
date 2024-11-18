array=[1,2,3,4,5,6,7,8,9]
def binary_search(arr,start,end,target):
    if start<end:
        mid=start+(end-start)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return binary_search(arr,mid,end,target)
        elif arr[mid]>target:
            return binary_search(arr,start,mid,target)
    else:
        return -1
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
target=1
print(binary_search(array,0,len(array),target))
print(linear_search(array,target))