class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[0]*(len(arr)-1)
        for num in range(0,len(arr)-1):
            result[num] = max(arr[num+1::])
        result.append(-1)
        return result

        