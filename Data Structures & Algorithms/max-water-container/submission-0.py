class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width * height'
        # makes sense to start with the maximum width always, we don't know
        # what the maximum height for two different bars is
        left, right = 0, len(heights) - 1
        maximum = 0
        while (left < right):
            curArea = min(heights[left], heights[right]) * (right - left)
            maximum = max(maximum, curArea)
            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        return maximum