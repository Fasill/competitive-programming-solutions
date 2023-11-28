class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitiudes = [0]
        for i in range(len(gain)):
            altitiudes.append(gain[i]+altitiudes[i])
        return max(altitiudes)  

