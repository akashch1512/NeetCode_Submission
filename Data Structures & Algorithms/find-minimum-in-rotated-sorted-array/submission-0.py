class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] - nums[0] == len(nums) - 1:
            return nums[0]
        
        Start = 0
        End = len(nums) - 1
    
        while Start <= End:
            Mid = (Start + End) // 2

            if nums[Mid - 1] > nums[Mid]:
                break
            
            elif nums[Mid] > nums[End]:
                Start = Mid + 1

            elif nums[Mid] < nums[End]:
                End = Mid - 1
            
        return nums[Mid]