class sorting():
    def __init__(self,array):
        self.array=array
    def bubble_sort(self):
        for n in range(len(self.array)-1,0,-1):
            for i in range(n):
                if self.array[i]>self.array[i+1]:
                    self.array[i],self.array[i+1]=self.array[i+1],self.array[i]
a=[3,2,0,0,4,6]
sorter=sorting(a)
print(a)
sorter.bubble_sort()
print(a)