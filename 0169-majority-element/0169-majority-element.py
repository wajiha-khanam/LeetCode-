class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums)//2
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

            if freq[i] > count:
                return i

    # Time - O(n)
    # Space - O(n)
         
        # ans = -1
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         ans = num
        #     if ans == num:
        #         count += 1
        #     else:
        #         count -= 1
        # return ans
    # Time - O(n)
    # Space - O(1)
        

        