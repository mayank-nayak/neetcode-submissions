class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            distance = 0
            while stack and stack[-1][0] < temp:
                top = stack.pop()
                ans[top[1]] = idx - top[1]
            stack.append([temp,idx])
        return ans
