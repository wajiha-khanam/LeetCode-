class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        counter = Counter(arr)
        for i in counter.values():
            if i in s:
                return False
            else:
                s.add(i)
        return True
        
    # Time - O(n)
    # Space - O(k), k-no. of unique elements