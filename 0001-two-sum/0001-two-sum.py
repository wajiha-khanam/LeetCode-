# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return ([i, j])
    
# Time complexity - O(n**2)
# Space complexity - O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}

       for i , num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            seen[num] = i
        
