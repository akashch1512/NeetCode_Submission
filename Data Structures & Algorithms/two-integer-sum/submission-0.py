class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        index = 0
        
        for num in nums:
            if (target - num) in values:
                return [values[target - num], index]
                
            if num not in values:
                values[num] = index

            index += 1
        
        print(values)
        return []


