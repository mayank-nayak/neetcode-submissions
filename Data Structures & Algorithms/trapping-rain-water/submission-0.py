class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        area = 0
        while (left < right):
            if (height[left] < height[right]):
                leftMax = max(height[left], leftMax)
                if (height[left] < leftMax):
                    area += leftMax - height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                if (height[right] < rightMax):
                    area += rightMax - height[right]
                right -= 1

        return area