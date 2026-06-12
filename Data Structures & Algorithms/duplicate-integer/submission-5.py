class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = set()
        
        for element in nums:
            if element in history:
                return True
            history.add(element)
        
        return False
