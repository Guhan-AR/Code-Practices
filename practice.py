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
# class Solution:
#     def canJump(self, nums: list[int]) -> bool:
#         index=len(nums)-1
#         for i in range(len(nums)-2,-1,-1):
#             print("for loop:",i)
#             print("index:",index,"i+nums[i]",i+nums[i])
#             if index == i + nums[i]:
#                 print("varuthu ippo:",i)
#                 index=i
#         return index == 0
# s=Solution()
# print(s.canJump([2,3,1,1,4]))

# person_1=[1,10,20,30,30,0,30,20,15,5]
# person_2=[2,20,20,10,30,0,0,0,15,5]
# amount=100
# def check_person(A,B,amount):
#     if A+B!=0:
#         return A/(A+B)*amount
#     else:
#         return amount/2
# for i in range(len(person_1)):
#     print("i=",i,"ans:",check_person(person_1[i],person_2[i],amount),"ans:",check_person(person_2[i],person_1[i],amount),"total:",check_person(person_1[i],person_2[i],amount)+check_person(person_2[i],person_1[i],amount))

# def scores(string):
#     string=string.strip()
#     score=0
#     for i in range(len(string)):
#         if i+4 <= len(string) and string[i:i+4] == string[i:i+4][::-1]:
#             score+=5
#         if i+5 <= len(string) and string[i:i+5] == string[i:i+5][::-1]:
#             score+=10
#     return score
# string = "    ABABAAAA "
# print(scores(string))

# def vowel_convertion(string):
#     for i in string:
#         if i.lower() in ["a","e","i","o","u"]:
#             return str(i*len(string))
#     return string
# string="BOB"
# print(vowel_convertion(string))

# def change_alternate_element(array):
#     a=array
#     for i in range(len(array)//2):
#         if i%2!=0:
#             a[i],array[-(i+1)]=array[-(i+1)],a[i]
#     return a
# a=[1,2,3,4,5,6,7]
# print(change_alternate_element(a))

# def add_higher_index(array):
#     summer=0
#     maxi=0
#     for i in array:
#         for j in str(i):
#             maxi=max(maxi,int(j))
#         summer+=maxi
#         maxi=0
#     return summer
# a=[7,10,32]
# print(add_higher_index(a))

# class Solution:
#     def jump(self, nums: list[int]) -> int:
#         near = far = jumps = 0
#         while far < len(nums) - 1:
#             farthest = 0
#             for i in range(near, far + 1):
#                 farthest = max(farthest, i + nums[i])
#             near = far + 1
#             far = farthest
#             jumps += 1
#         return jumps
# s=Solution()
# print(s.jump([2,3,1,1,4]))

# def binary_search(array,target,high,low):
#     if low<=high:
#         mid = low+(high-low)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]>=target:
#             return binary_search(array,target,mid-1,low)
#         else:
#             return binary_search(array,target,high,mid+1)
#     return -1
# array = [1, 3, 5, 7, 9, 11]
# target = 7
# result = binary_search(array, target, len(array) - 1, 0)
# print(result)  # Output: 3 (index of the target 7)

# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         index,maxi=0,0
#         for i in range(len(citations)):
#             if citations[i]>maxi:
#                 maxi=citations[i]
#                 index=i
#         return index
# s=Solution()
# print(s.hIndex([3,0,6,1,5]))

# class Solution:
#     def hIndex(self, citations: list[int]) -> int:
#         papers = len(citations)
#         citation_buckets = [0] * (papers + 1)

#         for citation in citations:
#             print(citation,citation_buckets)
#             citation_buckets[min(citation, papers)] += 1
#         print(citation_buckets)

#         cumulative_papers = 0
#         for h_index in range(papers, -1, -1):
#             cumulative_papers += citation_buckets[h_index]
#             print("cumulative paper=",cumulative_papers)
#             if cumulative_papers >= h_index:
#                 return h_index
# s=Solution()
# print(s.hIndex([3,0,6,1,5]))

# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         lp=[1]*len(nums)
#         rp=[1]*len(nums)
#         for i in range(1,len(nums)):
#             lp[i]=lp[i-1]*nums[i-1]
#         for i in range(len(nums)-2,-1,-1):
#             rp[i]=rp[i+1]*nums[i+1]
#         result=[1]*len(nums)
#         for i in range(len(nums)):
#             result[i]=lp[i]*rp[i]
#         return result
# s=Solution()
# print(s.productExceptSelf([3,5,5]))

# def zero_finder():
#     a=1
#     count=0
#     for i in range(1,101):
#         a*=i
#     a=str(a)
#     for i in a[::-1]:
#         if i!="0":
#             break
#         count+=1
#     print(count)

# zero_finder()

# class muni_hari_krishnan():
#     def __init__(self):
#         self.Name="muni_hari_krishnan"
#         self.fan_of="TVK"
#     def details(self):
#         return self.Name
# M=muni_hari_krishnan()
# print(M.details())

# arr=[0,1,2,3,4,5]
# n=len(arr)
# sum=0
# for i in range(n):
#     print("hi")
#     if arr[i]%2!=0 and ((arr[i]**2)**1/2==arr[i]):
#         print("hi hlo")
#         sum+=(arr[i]**2)
#     print(sum)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next

# Helper function to create a linked list from a list
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test the function
# if __name__ == "__main__":
#     # Create linked lists from input numbers
#     l1 = create_linked_list([2, 4, 3])  # Represents 342
#     l2 = create_linked_list([5, 6, 4])  # Represents 465

#     # Instantiate the Solution class
#     solution = Solution()

#     # Call the function
#     result = solution.addTwoNumbers(l1, l2)

    # Convert the result linked list back to a list and print it
    # print("Result:", linked_list_to_list(result))  # Expected Output: [7, 0, 8]

# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         max_val,left,right=0,0,len(height)-1
#         while left<right:
#             max_val=max(max_val , (right-left) * min(height[left],height[right]))
#             if height[left] < height[right]:
#                 left+=1
#             else:
#                 right-=1
#         return max_val
# sol=Solution()
# print(sol.maxArea([1,8,6,2,5,4,8,3,7]))


# def a(n):
#     i = 0
#     while i<n:
#         yield i
#         i+=1

# for i in a(10):
#     print(i)

# my_list = [x * 2 for x in range(100)]
# my_generator = (x * 2 for x in range(100))
# # print(my_generator)

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:  # Generate indefinitely
#         yield a
#         a, b = b, a + b

# # Example usage (print the first 10 Fibonacci numbers)
# fib_gen = fibonacci_generator()
# for _ in range(10):
#     print(next(fib_gen))

def filter_data(data):
    for item in data:
        if item > 10:
            yield item
            # return [item]

def square_data(data):
    for item in data:
        # yield item * item
        return item

# Example usage
data = [5, 12, 8, 15, 3, 20]
filtered_data = filter_data(data)
# squared_data = square_data(filtered_data)
# print(filtered_data)
# for value in filtered_data:
#     print(value)
print(list(filtered_data))