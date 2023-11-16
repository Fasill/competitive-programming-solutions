# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
def f(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
                
    
#             return False
print(f( [3,2,4],6))
            
# x = [1,2]
# print(len(x))

# x= "adc"
# print(sorted(x))
