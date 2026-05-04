class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterToLastPos = {}
        left, right = 0, 0
        ans = 0
        while (right < len(s)):
            if (s[right] in letterToLastPos):
                left = max(left, letterToLastPos[s[right]] + 1)
            letterToLastPos[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans