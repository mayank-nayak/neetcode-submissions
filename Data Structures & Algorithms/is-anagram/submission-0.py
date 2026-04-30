class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        letterDict = defaultdict(int)
        s = s.lower()
        t = t.lower()
        for i in range(0, len(s)):
            letterDict[s[i]] += 1
            letterDict[t[i]] -= 1
        for value in letterDict.values():
            if value != 0:
                return False

        return True

