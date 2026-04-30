class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToAnaMap = defaultdict(list)
        for s in strs:
            letterMap = [0] * 26
            for c in s:
                letterMap[ord(c.lower()) - ord('a')] += 1
            keyToAnaMap[tuple(letterMap)].append(s)
        outArr = []
        for key, val in keyToAnaMap.items():
            outArr.append(val)
        return outArr