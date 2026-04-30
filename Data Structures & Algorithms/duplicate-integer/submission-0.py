class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        print(counter)
        for key in counter:
            if (counter[key] > 1):
                return True
        return False
