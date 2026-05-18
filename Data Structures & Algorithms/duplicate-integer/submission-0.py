class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()

        for element in nums:
            if element in d:
                return True
            d[element] = 1
        
        return False

        