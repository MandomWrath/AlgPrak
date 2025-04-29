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
