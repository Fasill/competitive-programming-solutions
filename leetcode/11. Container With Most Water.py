class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        max_area = 0
        while l<=r:
            if height[l]>=height[r]:
                area = height[r]*(r-l)
                max_area = max(max_area,area)
                r-=1
            else:
                area = height[l]*(r-l)
                max_area = max(max_area,area)
                l+=1
        return max_area


#BRUTE FORCE
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         x = 0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 if height[i]<=height[j]:
#                     area = height[i]*(j-(i))
#                     if area > x:
#                         x = area
#                 else:
#                     area = height[j]*(j-(i))
#                     if area > x:
#                         x = area

#         return x
