# def merge_sort(arr):
#     if len(arr)>1:
#         left_arr = arr[:len(arr)//2]
#         right_arr = arr[len(arr)//2:]
#         merge_sort(left_arr)
#         merge_sort(right_arr)
#         i=j=k=0
#         while i<len(left_arr) and j<len(right_arr):
#             if left_arr[i]<right_arr[j]:
#                 arr[k]=left_arr[i]
#                 i+=1
#             else:
#                 arr[k]=right_arr[j]
#                 j+=1
#             k+=1
#         while i<len(left_arr):
#             arr[k]=left_arr[i]
#             i+=1
#             k+=1
#         while j<len(right_arr):
#             arr[k]=right_arr[j]
#             j+=1
#             k+=1
# a=[0,2,5,1,6]
# merge_sort(a)
# print(a)

# def sum_to_n(n):
#     # Base case
#     if n == 0:
#         return 0
#     # Recursive case
#     return n + sum_to_n(n - 1)
# print(sum_to_n(2))

def partition(arr,low,high):
    print(arr)
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            swap(arr,j,i)
    swap(arr,i+1,high)
    return i+1
def swap(arr,j,i):
    arr[j],arr[i]=arr[i],arr[j]
def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
a=[1,8,5,3,9]
print(a)
quick_sort(a,0,len(a)-1)
print("final:",a)