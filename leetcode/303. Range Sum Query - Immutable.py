class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = []
        c = 0
        for i in nums:
            c += i
            self.prefixes.append(c)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixes[right]-0
        else:
            return self.prefixes[right]-self.prefixes[left-1]



