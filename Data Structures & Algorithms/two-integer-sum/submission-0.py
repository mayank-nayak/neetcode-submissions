class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToDiffMap = {}
        ans = []
        for idx, num in enumerate(nums):
            if ((target - num) in numToDiffMap):
                ans = [numToDiffMap[(target - num)], idx]
                break
            numToDiffMap[num] = idx
        return ans

