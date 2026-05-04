from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        freqToNumArr = [0] * (len(nums) + 1)
        ans = []
        # build the freqToNumArr map
        for num, val in freqMap.items():
            if (freqToNumArr[val] == 0):
                freqToNumArr[val] = []
            freqToNumArr[val].append(num)
        for i in range(len(nums), -1, -1):
            if (len(ans) == k):
                break
            if (freqToNumArr[i] != 0):
                ans.extend(freqToNumArr[i])
        return ans