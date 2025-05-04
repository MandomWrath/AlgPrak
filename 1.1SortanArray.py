#merge
class Solution:
    def mergeArray(self,a,b):
        c=[]
        D=len(a)
        E=len(b)
        i,j=0,0
        while i<D and j<E:
            if a[i]<=b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        while i < D:
            c.append(a[i])
            i += 1
        while j < E:
            c.append(b[j])
            j += 1
        return c
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)//2
        a1=nums[:n]
        a2=nums[n:]
        if len(a1)>1:
            a1=self.sortArray(a1)
        if len(a2)>1:
            a2=self.sortArray(a2)
        return self.mergeArray(a1,a2)
\\\\\\\\\\\\\\\\\\\\
#quick 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        n=random.choice(nums)
        a=[x for x in nums if x < n]
        c=[x for x in nums if x==n]
        b=[x for x in nums if x>n]
        return self.sortArray(a) +c + self.sortArray(b)

\\\\\\\\\\\
#heap
class Solution:
    def HeapArray(self,nums,n,i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left < n and nums[left] >nums[largest]:
            largest = left
        if right < n and nums[right] >nums[largest]:
            largest = right
        if largest !=i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.HeapArray(nums,n,largest)
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n//2-1,-1,-1):
            self.HeapArray(nums,n,i)
        for i in range(n-1,0,-1):
            nums[0], nums[i] = nums[i], nums[0]
            self.HeapArray(nums,i,0)
        return nums

