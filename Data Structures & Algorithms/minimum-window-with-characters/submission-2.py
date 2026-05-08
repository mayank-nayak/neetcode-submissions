class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def charIndex(c):
            if c.islower():
                return ord(c) - ord('a')
            else:
                return ord(c) - ord('A') + 26

        def checkMatch(s, t):
            for j in range(52):
                if s[j] < t[j]:
                    return False
            return True

        if len(s) < len(t):
            return ""

        left, right = 0, 0
        sFreq, tFreq = [0] * 52, [0] * 52
        outLeft, outRight = 0, 0
        found = False
        minLength = len(s) + 1

        for i in range(len(t)):
            tFreq[charIndex(t[i])] += 1

        while right < len(s):
            if tFreq[charIndex(s[right])] > 0:
                sFreq[charIndex(s[right])] += 1

            if checkMatch(sFreq, tFreq):
                found = True
                while right - left + 1 >= len(t):
                    if tFreq[charIndex(s[left])] > 0:
                        if sFreq[charIndex(s[left])] - 1 < tFreq[charIndex(s[left])]:
                            break
                        sFreq[charIndex(s[left])] -= 1
                    left += 1

                if right - left + 1 <= minLength:
                    minLength = right - left + 1
                    outLeft, outRight = left, right

            right += 1

        if found:
            return s[outLeft:outRight + 1]
        return ""