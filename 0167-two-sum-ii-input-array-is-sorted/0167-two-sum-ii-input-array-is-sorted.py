class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return ([i+1,j+1])

        # seen = {}
        # for i, num in enumerate(numbers):
        #     if target-num in seen:
        #         return [seen[target-num]+1,i+1]
        #     seen[num] = i

        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]

        
            
            

        