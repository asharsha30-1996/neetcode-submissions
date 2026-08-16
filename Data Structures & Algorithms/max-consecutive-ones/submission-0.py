class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        store,count = 0,0
        for i in range (0,len(nums)):
            if nums[i]==1:
                count+=1
                store=max(count,store)
            else:
                count=0
        return store

                
        