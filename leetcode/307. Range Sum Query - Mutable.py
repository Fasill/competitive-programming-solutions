class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixes = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update_prefix(i + 1, nums[i])

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.update_prefix(index + 1, delta)

    def update_prefix(self, index: int, delta: int) -> None:
        while index < len(self.prefixes):
            self.prefixes[index] += delta
            index += index & -index

    def get_prefix(self, index: int) -> int:
        result = 0
        while index > 0:
            result += self.prefixes[index]
            index -= index & -index
        return result

    def sumRange(self, left: int, right: int) -> int:
        return self.get_prefix(right + 1) - self.get_prefix(left)
