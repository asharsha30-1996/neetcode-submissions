class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            complement=target-nums[i]
            if complement in nums:
                j=nums.index(complement)
                if i!=j:
                    return sorted([i,j])
            