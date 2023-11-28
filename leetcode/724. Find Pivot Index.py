class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        x = [0]
        for i in nums:
            x.append(i)
        for i in range(1, len(x)):

            if sum(x[:i]) == sum(x[i + 1:]):
                return i - 1
        return -1



