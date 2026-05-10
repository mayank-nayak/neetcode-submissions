class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairArr = [(p, s) for p, s in zip(position, speed)]
        pairArr.sort(reverse = True)
        localMax = (target - pairArr[0][0]) / pairArr[0][1] - 1
        fleets = 0
        for p, s in pairArr:
            currTime = (target - p) / s
            if (currTime > localMax):
                localMax = currTime
                fleets += 1
        return fleets
