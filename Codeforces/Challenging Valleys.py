def is_valley_sequence(nums):
    nums = [int(i) for i in nums]
    left = 0
    right = len(nums) - 1
    minimum = min(nums)

    while left < right:
        if nums[right] >= nums[left]:
            if nums[right] < nums[right - 1]:
                return "NO"
            right -= 1
        elif nums[right] < nums[left]:
            if nums[left] < nums[left + 1]:
                return "NO"
            left += 1

    return "YES"


x = int(input())
for i in range(x):
    n = input()
    nums = input().split()
    print(is_valley_sequence(nums))
