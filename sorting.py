class sorting():
    def __init__(self,array):
        self.array=array
    def bubble_sort(self):
        for n in range(len(self.array)-1,0,-1):
            for i in range(n):
                if self.array[i]>self.array[i+1]:
                    self.array[i],self.array[i+1]=self.array[i+1],self.array[i]
    def selection_sort(self):
        for i in range(len(self.array)):
            min_element=i
            for j in range(i,len(self.array)):
                if self.array[j]<self.array[min_element]:
                    min_element=j
            self.array[i],self.array[min_element]=self.array[min_element],self.array[i]
    def insertion_sort(self):
        for i in range(1,len(self.array)):
            key=self.array[i]
            j=i-1
            while j>=0 and key<self.array[j]:
                self.array[j+1]=self.array[j]
                j-=1
            self.array[j+1]=key
    def merge_sort(self,array=None):
        if array is None:
            array=self.array
        if len(array)>1:
            left_arr=array[:len(array)//2]
            right_arr=array[len(array)//2:]
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            i=j=k=0
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<right_arr[j]:
                    array[k]=left_arr[i]
                    i+=1
                else:
                    array[k]=right_arr[j]
                    j+=1
                k+=1
            while i<len(left_arr):
                array[k]=left_arr[i]
                i+=1
                k+=1
            while j<len(right_arr):
                array[k]=right_arr[j]
                j+=1
                k+=1

a=[3,2,0,0,4,6]
sorter=sorting(a)
print("Before sorting:",a)
sorter.merge_sort()
print("After sorting:",a)