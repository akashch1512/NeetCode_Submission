class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        
        for index, num in enumerate(nums):
            if (target - num) in values:
                return [values[target - num], index]

            if num not in values:
                values[num] = index

            index += 1
        
        return values


