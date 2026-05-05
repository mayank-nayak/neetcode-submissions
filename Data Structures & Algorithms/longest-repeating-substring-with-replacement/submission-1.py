class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        mostFreq, longest = 0, 0
        freqMap = {}
        while (right < len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            mostFreq = max(mostFreq, freqMap[s[right]])
            if (right - left + 1 - mostFreq > k):
                freqMap[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest