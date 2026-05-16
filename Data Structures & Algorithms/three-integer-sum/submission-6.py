class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        nums.sort()

        # [-4, -1, -1, 0, 1, 2]
        for k, num3 in enumerate(nums): # Target is -k
            left = k + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum == -num3 and [nums[left], nums[right], num3] not in answer:
                    answer.append([nums[left], nums[right], num3])
                    right -= 1
                    left += 1
                    
                elif curr_sum > -num3:
                    right -= 1

                else:
                    left += 1
        
        return answer
            
