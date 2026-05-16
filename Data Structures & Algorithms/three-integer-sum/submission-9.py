class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        nums.sort()

        # [-2,0,0,2,2] [-1,0,1,2,-1,-4]
        for k, num3 in enumerate(nums): # Target is -k
            if (k != 0) and (num3 == nums[k - 1]):
                continue

            left = k + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum == -num3:
                    answer.append([nums[left], nums[right], num3])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif curr_sum > -num3:
                    right -= 1

                else:
                    left += 1
        
        return answer
            
