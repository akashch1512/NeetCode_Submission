class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Less memory by using set just for checking
        l = set()

        for element in nums:
            if element in l:
                return True
            l.add(element)
        
        return False

        