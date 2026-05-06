class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        s1Map = [0] * 26
        s2Map = [0] * 26
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if (s1Map[i] == s2Map[i]):
                matches += 1
        if (matches == 26):
            return True
        left, right = 0, len(s1)
        while (right < len(s2)):
            if (matches == 26):
                return True

            rightIndex = ord(s2[right]) - ord('a')
            leftIndex = ord(s2[left]) - ord('a')
            left += 1
            s2Map[rightIndex] += 1
            if (s2Map[rightIndex] == s1Map[rightIndex]):
                matches += 1
            elif (s2Map[rightIndex] - 1 == s1Map[rightIndex]):
                matches -= 1
            s2Map[leftIndex] -= 1
            if (s2Map[leftIndex] == s1Map[leftIndex]):
                matches += 1
            elif (s2Map[leftIndex] + 1 == s1Map[leftIndex]):
                matches -= 1
            right += 1

        return matches == 26

