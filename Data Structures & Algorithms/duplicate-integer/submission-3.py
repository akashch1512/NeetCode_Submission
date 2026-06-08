class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = dict()
        for element in nums:
            if element in history:
                return True
            history[element] = history.get(element, 0) + 1
        
        return False
