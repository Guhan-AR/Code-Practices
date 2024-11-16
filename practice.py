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

# def partition(arr,low,high):
#     print(arr)
#     pivot=arr[high]
#     i=low-1
#     for j in range(low,high):
#         if arr[j]<pivot:
#             i+=1
#             swap(arr,j,i)
#     swap(arr,i+1,high)
#     return i+1
# def swap(arr,j,i):
#     arr[j],arr[i]=arr[i],arr[j]
# def quick_sort(arr,low,high):
#     if low<high:
#         pi=partition(arr,low,high)
#         quick_sort(arr,low,pi-1)
#         quick_sort(arr,pi+1,high)
# a=[1,8,5,3,9]
# print(a)
# quick_sort(a,0,len(a)-1)
# print("final:",a)

# def open_close_brace_checks(b):
#     stack=[]
#     for i in b:
#         if i in ["(","[","{"]:
#             stack.append(i)
#         elif (i=="]")and(stack[-1]!="[") or (i=="}") and (stack[-1]!="{") or (i==")") and (stack[-1]!="("):
#             return False
#         else:
#             stack.pop()
#     return not stack
# a="({[]()})"
# b="({]})"
# c="()()()()[]"
# d="[]{()}"
# print(open_close_brace_checks(a))
# print(open_close_brace_checks(b))
# print(open_close_brace_checks(c))
# print(open_close_brace_checks(d))

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack=[]
#         brace={")":"(","}":"{","]":"["}
#         for i in s:
#             print(stack)
#             if i in brace.values():
#                 stack.append(i)
#             elif i in brace.keys():
#                 if not stack or brace[i]!=stack.pop():
#                     return False
#         return not stack
# sol=Solution()
# print(sol.isValid(a))
# print(sol.isValid(b))
# print(sol.isValid(c))
# print(sol.isValid(d))

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(1,len(arr)):
#             if arr[j]<arr[j-1]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]
# def swap(arr,i,j):
#     arr[i],arr[j]=arr[j],arr[i]
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index=i
#         for j in range(i+1,len(arr)):
#             if arr[min_index]>arr[j]:
#                 min_index=j
#         swap(arr,min_index,i)
# def merge_sort(arr):
#     if len(arr)>1:
#         left_arr=arr[:len(arr)//2]
#         right_arr=arr[len(arr)//2:]
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
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
# a=[0,4,2,6,8]
# # insertion_sort(a)
# # print(a)
# def partition(arr,low,high):
#     pivot=arr[high]
#     i=low-1
#     for j in range(low,high):
#         if arr[j]<pivot:
#             i+=1
#             # swap(arr,j,i)
#             arr[i],arr[j]=arr[j],arr[i]
#         # swap(arr,high,i+1)
#     arr[high],arr[i+1]=arr[i+1],arr[high]
#     return i+1
# def quick_sort(arr,low,high):
#     if low < high:
#         pivot=partition(arr,low,high)
#         quick_sort(arr,low,pivot-1)
#         quick_sort(arr,pivot+1,high)
# a=[0,4,2,6,8]
# quick_sort(a,0,len(a)-1)
# print(a)

# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         i,j,k=m-1,n-1,m+n-1
#         while i>=0 and j>=0:
#             if nums1[i]>nums2[j]:
#                 nums1[k]=nums1[i]
#                 i-=1
#                 k-=1
#             else:
#                 nums1[k]=nums2[j]
#                 j-=1
#                 k-=1
#         while j>=0:
#             nums1[k]=nums2[j]
#             j-=1
#             k-=1
# a=[1,2,7,0,0,0]
# b=[3,8,9]
# sol=Solution()
# sol.merge(a,3,b,3)
# print(a)

# class Solution:
#     def removeDuplicates(nums: list[int]) -> int:
#         if len(nums)<=2:
#             return len(nums)
#         write_index=2
#         for i in range(2,len(nums)):
#             if nums[i]!=nums[write_index-2]:
#                 nums[write_index]=nums[i]
#                 write_index+=1
#         return write_index
            

            
# a=Solution
# c=[0,0,1,1,1,1,2,3,3]
# b=a.removeDuplicates(c)
# print(b) # output 7
# print(c) # output [0,0,1,1,2,3,3]
# print(c[:b])

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         d={}
#         max_ele=count=0
#         for i in nums:
#             if i in d:
#                 d[i]+=1
#                 if d[i]>count:
#                     count=d[i]
#                     max_ele=i
#             else:
#                 d[i]=1
#         return max_ele

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k=k%len(nums)
#         nums=nums[len(nums)-k:]+nums[:len(nums)-k]
#         print(nums)
# sol=Solution()
# sol.rotate([1,2,3,4,5,6],10)

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         max_prize=0
#         min_prize=prices[0]
#         for j in range(1,len(prices)):
#             max_prize=max(max_prize,prices[j]-min_prize)
#             min_prize=min(prices[j],min_prize)
#         return max_prize
# sol=Solution()
# prices = [[7,1,5,3,6,4],[7,6,4,3,1]]
# for i in prices:
#     b=sol.maxProfit(i)
#     print(b)
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         amount=0
#         for i in range(1,len(prices)):
#             if prices[i-1]<prices[i]:
#                 amount+=prices[i]-prices[i-1]
#         return amount
# a=[6,1,3,2,4,7]
# s=Solution()
# b=s.maxProfit(a)
# print(b,7)
# a=10
# for i in range(a//2-1,-1,-1):
#     print(i)
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        index=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            print("for loop:",i)
            print("index:",index,"i+nums[i]",i+nums[i])
            if index == i + nums[i]:
                print("varuthu ippo:",i)
                index=i
        return index == 0
s=Solution()
print(s.canJump([2,3,1,1,4]))