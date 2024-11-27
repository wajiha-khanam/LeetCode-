class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [ False for _ in range(len(candies)) ]
        currMaxcandies = max(candies)

        for i, currCandies in enumerate(candies):
            if (currCandies + extraCandies >= currMaxcandies):
                result[i] = True
        return result
    # Time - O(n)
    # Space - O(n)