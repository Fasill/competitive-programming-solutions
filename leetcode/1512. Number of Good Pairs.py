
def goodPairs(nums):
    x = 0
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
           if nums[i] == nums[j]:
               x+=1
    return(x)

nums = [1,1,1,1]
print(goodPairs(nums))